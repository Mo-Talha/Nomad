"""
This file is dedicated to removing redundant/useless information about job summaries.
"""

remove = [
    """
    IMPORTANT NOTE ABOUT EMPLOYMENT AUTHORIZATIONS:

    It is the student's responsibility to ensure that they have the necessary documentation required by the country the job
    is in to participate in this co-op work term. The University cannot provide related advice or arrange for this
    documentation on a student's behalf. The student must work with the employer and/or the issuing authority of the
    destination country to obtain this documentation. If the student cannot obtain the necessary documentation to
    participate in the co-op work term, the student must find an alternate co-op opportunity. Working in a country without
    the necessary documentation can have serious consequences, including, but without limitation, being fined or detained.
    Any consequences that ensue from having inappropriate documentation are the student's responsibility.
    """,
    """
    *NOTE FROM CECA RE: EMPLOYMENT BASED IN THE USA*
    This work opportunity will be based in the USA; therefore all applicants must determine whether they are
    eligible to work in the USA. To assess your eligibility please go to https://uwaterloo.ca/co-operative-education
    /working-abroad/finding-international-job-opportunities/are-you-eligible-work-abroad and read the information
    listed in its entirety before you apply for this job.

    For specific information on the USA visa process that affects co-op employment, please refer to
    http://uwaterloo.ca/co-operative-education/working-abroad/work-permits-international-co-op-work-terms/usa-work-permitj-1-visa.

    Before you apply to this job, please be aware of mandatory and other requirements for students working outside
    Canada: https://uwaterloo.ca/co-operative-education/working-abroad/found-international-job-jobmine
    """,
    """
    *IMPORTANT NOTE FROM CECA RE: EMPLOYMENT OUTSIDE Canada and USA *

    This work opportunity will be outside Canada and USA, and therefore will have certain financial realities.
    Students should be aware that student salaries in countries outside North America are typically significantly
    lower than Canadian minimum wages, and that it is unlikely that the local salary will allow for any significant level
    of savings during the work term.

    Also, international companies do not necessarily provide any additional compensation for airfare, work permit or
    housing expenses. Sign-offs will not be permitted for financial reasons; so, please review what is covered or
    not covered in the compensation details. Use a currency converter like http://www.bankofcanada.ca/rates/exchange
    /daily-converter/  to understand the Canadian equivalent.  Students should assume that all expenses related to airfare,
    work permit and housing will be the responsibility of the student.

    Also, please go to https://uwaterloo.ca/co-operative-education/working-abroad/finding-international-job-opportunities
    /are-you-eligible-work-abroad, and read the information listed in its entirety before you apply for this job. Please
    be aware of mandatory and other requirements for students working outside Canada: https://uwaterloo.ca/co-operative
    -education/working-abroad/found-international-job-jobmine.

    Co-op students who are successful in obtaining an international co-op work term can consider applying for international
    travel awards /scholarships detailed at Student Awards and Financial Aid (SAFA): https://uwaterloo.ca/student-awards
    -financial-aid/international-experience-awards. Apply as early as possible as applications have deadlines - see
    SAFA site for details.
    """
]

# Test summary from random job
test_summary = """
*** PLEASE NOTE:

The University has heard that students who are not Chinese nationals have had significant challenges acquiring necessary employment authorizations for work terms in China. We advise you to contact the Chinese immigration authority as soon as possible to ensure you are eligible for the necessary employment authorizations. ***

IMPORTANT NOTE ABOUT EMPLOYMENT AUTHORIZATIONS:

It is the student's responsibility to ensure that they have the necessary documentation required by the country the job is in to participate in this co-op work term. The University cannot provide related advice or arrange for this documentation on a student's behalf. The student must work with the employer and/or the issuing authority of the destination country to obtain this documentation. If the student cannot obtain the necessary documentation to participate in the co-op work term, the student must find an alternate co-op opportunity. Working in a country without the necessary documentation can have serious consequences, including, but without limitation, being fined or detained. Any consequences that ensue from having inappropriate documentation are the student's responsibility.

******************************************************************************************
About Us

Based in Shanghai, Collective Responsibility is one of Asia's most recognized authorities on sustainability, innovation and responsible leadership.

Founded with the fundamental belief that a sustainable world can only be achieved through awareness of issues, finding tangibility in business cases and development of cross-sector collaboration, Collective Responsibility acts as a knowledge base, catalyst and facilitator between stakeholders.

Through consulting, research, training and enabling cross platform discussions, we aim to:

- Create a knowledge base and catalyze discussion of issues related to the development of civil society, business sustainability and social development in Asia.
- Develop tangible interests, engagement and action on issues of sustainability (economic, environmental and societal).
- Build bridges between local and foreign resources to ensure knowledge transfer, program scalability and growth.
- Develop organisational capacity with the aim to help create stable and profitable enterprises.

Position: Research Analyst Intern

The Research Analyst will be involved in high level research on issues related to sustainability, social entrepreneurship and leadership development.
Responsibilities include:

-  Researching social, environmental, and economic issues
-  Development of our knowledge base is key to our ability to inform and advise corporate decision makers.
-  Analysts will be tasked with research projects, which will be used in programs, events, with key highlights sent to our members network.
-  Conduct interviews and write profiles of people and programs
-  To understand the requirements of our clients, we have to meet and speak with them about the challenges they are facing as well as the opportunities that they have identified but need help executing.
-  The analyst will help with designing and conducting interviews to leaders in corporate sustainability, and write up the interviews for publication on our website and newsletter.
-  The analyst will also research and add to a database of sustainability leaders to interview across Asia-Pacific.

Requirements:

-  Major in sociology, economics, civil affairs, environment, or other sustainability related fields.
-  Fluency in spoken and written English.
-  Outgoing, hardworking and passionate about helping others.
-  Enjoy working in an international team with diverse skills.
-  Strong computer skills (Word, Excel and Power point).
-  Knowledge of a data analysis and modelling software (R, SPSS, Mat Lab) is an advantage.
-  Proficiency in Mandarin is an advantage, but not a necessity.

Skill Development:

-  How to develop, plan and structure reports for white paper publication
-  Development of data analysis skills, working with vast data sets and using excel to an advanced level.
-  How to present data in a digestible form for maximum impact
-  How to work with a diverse group of people with differing skill sets and academic backgrounds
-  A holistic approach to problem solving and analysis
-  Specific understanding of China's challenges and the implications of its environmental and economic activity
-  A strong cultural experience and understanding of a foreign way of life and practice

Please apply on JobMine AND  send a resume and cover letter to charlie@coresponsibility.com

***************************************************************************************

*IMPORTANT NOTE FROM CECA RE: EMPLOYMENT OUTSIDE Canada and USA *

This work opportunity will be outside Canada and USA, and therefore will have certain financial realities.  Students should be aware that student salaries in countries outside North America are typically significantly lower than Canadian minimum wages, and that it is unlikely that the local salary will allow for any significant level of savings during the work term.

Also, international companies do not necessarily provide any additional compensation for airfare, work permit or housing expenses. Sign-offs will not be permitted for financial reasons; so, please review what is covered or not covered in the compensation details. Use a currency converter like http://www.bankofcanada.ca/rates/exchange/daily-converter/  to understand the Canadian equivalent.  Students should assume that all expenses related to airfare, work permit and housing will be the responsibility of the student.

Also, please go to https://uwaterloo.ca/co-operative-education/working-abroad/finding-international-job-opportunities/are-you-eligible-work-abroad, and read the information listed in its entirety before you apply for this job. Please be aware of mandatory and other requirements for students working outside Canada: https://uwaterloo.ca/co-operative-education/working-abroad/found-international-job-jobmine.

Co-op students who are successful in obtaining an international co-op work term can consider applying for international travel awards /scholarships detailed at Student Awards and Financial Aid (SAFA): https://uwaterloo.ca/student-awards-financial-aid/international-experience-awards. Apply as early as possible as applications have deadlines - see SAFA site for details.
***************************************************************************************************
"""