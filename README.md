# PROBLEM STATEMENT

•	There is an ‘Employee’ service which provides endpoints to create, update and get employees details.
 
 
•	There is a ‘Dashboard’ which is exposed to HRs that internally calls the ‘Employee’ service APIs, lets call this dashboard as consumer of employee service.
•	A scalable test approach needs to be created that:
#	Creates a contract of both the services (dashboard and employee). 
[]	Consumer contract for Dashboard service and Provider contract for Employee service.

[]	Note: Contract represents A document that contains the expected mocked Http response on a mocked Http request.

[]	Use pact-python (Python library) to generate the contracts.

#	Write test cases. 
[]	To allow Consumer contract to be created only if Provider contract exists otherwise fail.

[]	Consumer contract should always be the subset of the Provider contract.

[]	As soon as there is change in APIs of provider, contract needs to be updated and updated contract needs to be checked that it is not breaking any Consumer contract.
 


