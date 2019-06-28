* Part
	* partNumber
	* materialType (ie: sheet metal, bar stock, etc.)
	* material (ie: carbon steel, stainless, etc.)
		* idReference (reference to standards)
	* gauge
		* idReference (reference to standards)
	* blank (ie: 20x50 16GA, etc.)
		* width
		* height
		* laserPath
		* weight
	* partProcesses (ie: press brake, laser, machining, etc.)
		* processCategory
		* operationNumber
		* operationName
		* workCenterID
		* setup
		* operationTime
		* operationQuantity

* Maintenance
	* Update rates, materials, process
		* materialType
		* material
			* Material type
			* Material Name
			* Material Densities
		* gauge
			* gaugeName
			* gaugeThickness
		* processCategory
			* processCategoryName
			* defaultRate
			* defaultOverhead
			* defaultTP
			* unitsTP
			* defaultSetup
		* workCenter
			* workCenterID
			* workCenterName
			* processCategory
			* hourlyRate
			* hourlyOverhead
			* estimatedTP
			* estimatedSetup