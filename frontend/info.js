async function getData() {
    const response=await fetch("https://restcountries.com/v2/all")
    const countriesData=await response.json()
    return countriesData
}

async function displaycountriesTable(){
    const countries=await getData()
    console.log(countries)
    
    const countryTableBody = document.getElementById('countries-table-body')
    for(let country of countries){
        const row =document.createElement('tr')
        const nameCell=document.createElement('td')
        nameCell.textContent=country.name
        row.appendChild(nameCell)


        const flagCell=document.createElement('td')
        const flagImg=document.createElement('img')
        flagImg.src=country.flag
        flagCell.appendChild(flagImg)
        row.appendChild(flagCell)


        const populationCell=document.createElement('td')
        populationCell.textContent=(country.population/1000000).toFixed(2)
        row.appendChild(populationCell)


        const areaCell=document.createElement('td')
        areaCell.textContent=(country.area/1000).toFixed(2)
        row.appendChild(areaCell)


        const codecallingCell=document.createElement('td')
        codecallingCell.textContent="+" +country.codeCodes[0]
        row.appendChild(codecallingCell)


        const capitalCell=document.createElement('td')
        capitalCell.textContent=country.capital
        row.appendChild(capitalCell)

        const languagesCell=document.createElement('td')
        const languagesList=country.languages.map(language=>language.)
        languagesCell.textContent=country.languagesList
        row.appendChild(languagesCell)

    
        countryTableBody.appendChild(row)
   
    } 
}

displaycountriesTable ()