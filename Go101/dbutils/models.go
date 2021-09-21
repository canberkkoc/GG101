package dbutils

type Cities struct {
	Id   int64  `json:"id" gorm:"primaryKey;autoIncrement:true"`
	Name string `json:"name"`
}

type Wildfires struct {
	Id        int64   `json:"id" gorm:"primaryKey;autoIncrement:true"`
	Status    string  `json:"status"`
	RiskLevel string  `json:"risk_level"`
	FireType  string  `json:"type"`
	Cause     string  `json:"cause"`
	Locationx float32 `json:"locationx"`
	Locationy float32 `json:"locationy"`
	Time      string  `json:"time"`
	District  string  `json:"district"`
	City      int64   `json:"city"`
	Cities    Cities  `gorm:"ForeignKey:City;References:Id"`
}
