// wildfires
package main

import (
	"Go101/dbutils"
	"fmt"
	"html/template"
	"io"
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
)

type TemplateRenderer struct {
	templates *template.Template
}

func (t *TemplateRenderer) Render(w io.Writer, name string, data interface{}, c echo.Context) error {
	return t.templates.ExecuteTemplate(w, name, data)
}

func GetCities(c echo.Context) error {
	cities, err := GetCitiesFromDb()
	if err != nil {
		return c.JSON(http.StatusNotFound, err)
	}
	return c.Render(http.StatusOK, "index.html", cities)
}

func GetCitiesFromDb() ([]dbutils.Cities, error) {
	db := dbutils.GetDBInstance()
	cities := []dbutils.Cities{}
	if err := db.Find(&cities).Error; err != nil {
		return nil, err
	}

	return cities, nil
}

func GetWildfires(c echo.Context) error {
	wildfires, err := GetWildfiresFromDb(c.Param("id"))
	if err != nil {
		return c.JSON(http.StatusNotFound, err)
	}
	return c.Render(http.StatusOK, "fires.html", wildfires)
}

//  func GetWildfiresFromDb(Id string) (interface{}, error) can used like this 
func GetWildfiresFromDb(Id string) ([]dbutils.Wildfires, error) {
	db := dbutils.GetDBInstance()
	fmt.Println(Id)
	CityId, _ := strconv.ParseInt(Id, 10, 64)
	fmt.Print(CityId)
	wildfires := []dbutils.Wildfires{}
	if err := db.Preload("Cities").Find(&wildfires, &dbutils.Wildfires{City: CityId}).Error; err != nil {
		return nil, err
	}
	return wildfires, nil
}

func main() {
	e := echo.New()

	dbutils.NewDB()
	t := &TemplateRenderer{
		templates: template.Must(template.ParseGlob("*.html")),
	}
	e.Renderer = t
	e.GET("/", GetCities)

	e.GET("/city/:id", GetWildfires)

	e.Logger.Fatal(e.Start(":8000"))
}
