from playwright.async_api import async_playwright
import asyncio
import os
import uuid
import streamlit as st # for session id
async def scrape_cdlt(plantype, state, pcode):
    async with async_playwright() as p:
        # Launch the browser
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Navigate to the URL
        await page.goto("https://clinicaldocumentationtool.anthem.com/cdltui/home")

        # Wait for the dropdown to be available and select options
        await page.wait_for_selector('select[formcontrolname="plantype"]')
        await page.select_option('select[formcontrolname="plantype"]', plantype)

        await page.select_option('select[formcontrolname="state"]', state)
        await page.wait_for_timeout(3000)
        await page.fill('input[formcontrolname="pcode"]', pcode)
        await page.wait_for_timeout(3000)
        await page.click("button.search_button")

        await page.wait_for_timeout(10000)

        # Locate all anchor tags containing the links
        links = await page.eval_on_selector_all("app-datatable a[href]", "anchors => anchors.map(anchor => anchor.href)")

        # Loop through each link and save it as an HTML file in the project directory
        unique_links = list(set(links))  # Remove duplicate links by converting to a set and back to a list
        for i, link in enumerate(unique_links):
            try:
                # Navigate to the link
                await page.goto(link, wait_until="load")

                # # Fetch the content of the page
                # content_full = await page.content()

                # # Because the language model does not handle too long a text.
                # content = content_full[:1000]

                # Extract the text content of the page (no html)
                text_content = await page.evaluate("document.body.innerText")

                # Cause GPT-4 does not handle too long a text.
                content = text_content[:6000]
                # Set the file name
                if 'session_id' not in st.session_state:
                    st.session_state['session_id'] = str(uuid.uuid4())
                session_id = st.session_state['session_id']
                user_docs_folder = os.path.join(os.getcwd(), 'user-docs')
                os.makedirs(user_docs_folder, exist_ok=True)
                session_folder = os.path.join(user_docs_folder, session_id)
                os.makedirs(session_folder, exist_ok=True)
                file_path = os.path.join(session_folder, f"link_{i + 1}.txt")

                # Write the content to a file
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)

                print(f"Saved content of {link} to {file_path}")
            except Exception as e:
                print(f"Failed to navigate to {link}:", e)

        await page.wait_for_timeout(10000)
        await browser.close()

# Function to run the scraper
def run_scraper(plantype, state, pcode):
    print('run scraper called')
    print('*'*10)
    print(plantype, state, pcode)
    print('*'*10)
    asyncio.run(scrape_cdlt(plantype, state, pcode))

# run_scraper('Commercial', 'NY', '43775')

