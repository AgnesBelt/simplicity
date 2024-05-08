set UDC


param UDCMultiplierTotalCapacity
param UDCMultiplierNewCapacity
param UDCMultiplierActivity
param UDCConstant
param UDCTag


s.t. UDC0_UserDefinedConstraintEquality{r in REGION, u in UDC, y in YEAR: UDCTag[r,u] = 0}: 
sum{t in TECHNOLOGY}UDCMultiplierTotalCapacity[r,t,u,y]*TotalCapacityAnnual[r,t,y] + 
sum{t in TECHNOLOGY}UDCMultiplierNewCapacity[r,t,u,y]*NewCapacity[r,t,y] +
sum{t in TECHNOLOGY}UDCMultiplierActivity[r,t,u,y]*TotalTechnologyAnnualActivity[r,t,y] = UDCConstant[r,u,y];

s.t. UDC1_UserDefinedConstraintInequality{r in REGION, u in UDC, y in YEAR: UDCTag[r,u] = 1}: 
sum{t in TECHNOLOGY}UDCMultiplierTotalCapacity[r,t,u,y]*TotalCapacityAnnual[r,t,y] + 
sum{t in TECHNOLOGY}UDCMultiplierNewCapacity[r,t,u,y]*NewCapacity[r,t,y] +
sum{t in TECHNOLOGY}UDCMultiplierActivity[r,t,u,y]*TotalTechnologyAnnualActivity[r,t,y] >= UDCConstant[r,u,y];

s.t. UDC2_UserDefinedConstraintInequality{r in REGION, u in UDC, y in YEAR: UDCTag[r,u] = 2}: 
sum{t in TECHNOLOGY}UDCMultiplierTotalCapacity[r,t,u,y]*TotalCapacityAnnual[r,t,y] + 
sum{t in TECHNOLOGY}UDCMultiplierNewCapacity[r,t,u,y]*NewCapacity[r,t,y] +
sum{t in TECHNOLOGY}UDCMultiplierActivity[r,t,u,y]*TotalTechnologyAnnualActivity[r,t,y] <= UDCConstant[r,u,y];