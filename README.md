1. Find CPT code from EHR system (currently this is manually input into a form field)
2. Scraper system goes to cdlt tool and brings back the relevant documents + Recommended documents

3. Upload all documents (physician notes, diet charts, ~~EOC~~ etc.)
4. All of this (uploaded docs + um docs) is now sent to an LLM in 2 separate calls
5. LLM returns back the Missing Information and Recommendations sheet
   5.b - ~~If EOC covers the procedure, then proceed to next step~~ where the UM document + "Recommended Documents" is reviewed to check if all documentation is in order and if the patient is eligible for the procedure. In this step, the LLM outputs the list of missing documents etc.

The below has been postponed
~~5.a - Does the EOC cover the procedure (name only ... no cpt)? LLM needs to make the inference that gastric bypass is a type of bariatric surgery~~
