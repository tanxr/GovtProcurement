
import csv
import pandas as pd

filename = '/Users/xuanrong/mystuff/git/GovtProcurement/government-procurement/government-procurement-via-gebiz-2015.csv'
cols = ['Tender Number', 'Agency', 'Tender Description', 'Award Date', 'Tender Detail Status', 'Supplier Name', 'Total Awarded Amount']
gp = pd.read_csv(filename, header=0, names=cols)

Agency_set = set(gp['Agency'])

#cw = csv.writer(open("hello.csv",'wb'))
#cw.writerow(list(Agency_set))

with open('Agency_List_2.csv', 'wb') as f:
    writer = csv.writer(f)
    for val in Agency_set:
        writer.writerow([val])


"""
MCI
MCCY
MINDEF
MOE
MOF
MFA
MOH
MHA
MINLAW
MOM
MND
MSF
MEWR
MTI
MOT
PMO


Council for Private Education
Energy Market Authority of Singapore
Civil Service College
Competition Commission of Singapore
Singapore Examinations and Assessment Board
Ministry of the Environment and Water Resources
Singapore Tourism Board
Ministry of Manpower - Foreign Manpower Management Division
Ministry of Social and Family Development - Ministry Headquarter
NUS HIGH SCHOOL OF MATHEMATICS AND SCIENCE
ISEAS - Yusof Ishak Institute
Ministry of National Development-Ministry Headquarter
International Enterprise Singapore
Ministry of Manpower - Occupational Safety & Health Division
"Ministry of Culture, Community and Youth - Ministry Headquarter"
Science Centre Board
Tote Board
Accounting And Corporate Regulatory Authority
Prime Minister's Office-Ministry Headquarter
Ministry of Law-Ministry Headquarter
Nanyang Technological University
Ministry of Foreign Affairs
National Parks Board
Singapore Land Authority
National Arts Council
Temasek Polytechnic
Assumption Pathway School
Casino Regulatory Authority
Health Sciences Authority
Ministry of Manpower-Labour Relations Department
Civil Aviation Authority of Singapore
Ministry of Defence
Ministry of Health-Ministry Headquarter
Auditor-General's Office
Council for Estate Agencies
Prime Minister's Office-Corrupt Practices Investigation Bureau
"Ministry of Culture, Community and Youth - National Youth Council"
Ministry of Finance - Vital
Judiciary-Supreme Court
Raffles Girls' School (Secondary)
"School of Science and Technology, Singapore"
Central Provident Fund Board
Duke-NUS Medical School
Singapore Workforce Development Agency
National University of Singapore
Methodist Girls' School (Secondary)
National Heritage Board
Ministry of Social and Family Development - Family Development Group
Prime Minister's Office - National Security Co-ordination Secretariat
Ministry of Social and Family Development - Rehabilitation and Protection
Nanyang Polytechnic
Ministry of Trade & Industry-Ministry Headquarter
Maritime and Port Authority of Singapore
Majlis Ugama Islam Singapura
Republic Polytechnic
Ministry of Transport - Ministry Headquarter
Ministry of Finance - Singapore Customs
Singapore Chinese Girls' School
Singapore Polytechnic
Ngee Ann Polytechnic
Inland Revenue Authority of Singapore
Ministry of Education
Prime Minister's Office - National Research Foundation
Defence Science and Technology Agency
Urban Redevelopment Authority
Singapore Corporation of Rehabilitative Enterprises
Singapore Labour Foundation
Housing and Development Board
People's Association
Health Promotion Board
Ministry of Defence 5
National Library Board
Institute of Technical Education
Singapore Sports Council
Centre for Public Project Management
Monetary Authority of Singapore
Ministry of Finance-Ministry Headquarter
Economic Development Board
National Environment Agency
Sentosa Development Corporation
Attorney-General's Chambers
SPRING Singapore
Parliament
Jurong Town Corporation
Prime Minister's Office-Public Service Division
Building and Construction Authority
Productivity Fund Administration Board
Media Development Authority
Ministry of Manpower-Ministry Headquarter
Prime Minister's Office - National Population and Talent Division
Ministry of Social and Family Development - Early Childhood Development Agency
Istana
Northlight School
Ministry of Trade & Industry-Department of Statistics
Land Transport Authority
Infocommunications Development Authority of Singapore
Public Utilities Board
Prime Minister's Office - National Climate Change Secretariat
National Institute of Education
National Council of Social Service
Ministry of Communications and Information
"Agency for Science, Technology and Research"
Judiciary-State Courts
Agri-food and Veterinary Authority
Ministry of Finance-Accountant-General's Department
Prime Minister's Office-Elections Department
Ministry of Manpower-Information Systems & Technology Department
Intellectual Property Office of Singapore
Ministry of Home Affairs-Ministry Headquarter
"""
