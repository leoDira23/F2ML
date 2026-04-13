import axios from 'axios'

//url do nosso backend
const apiUrl = 'http://localhost:5000'


//o objeto que contem o serviço de autorização
const authService = {

    async authenticate(data){
        const endpoint = `${apiUrl}/login`
        return axios.post(endpoint,data);
    }
,

setLoggedUser(data){
    let parsedData = JSON.stringify(data)
    localStorage.setItem("user",parsedData)
},

getLoggedUser(){
    let data = localStorage.getItem("user")
    if(!data) return null
    try {
        let parseData = JSON.parse(data)
        return parseData
    } catch(error){
        console.log(error)
        return null
    }
}
}

export default authService


