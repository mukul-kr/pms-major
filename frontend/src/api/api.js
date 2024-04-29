import axios from 'axios';

const api = axios.create({
    baseURL: 'http://34.93.25.177:3000/',
});


api.interceptors.request.use((req) => {
    const cookies = document.cookie.split(';');
    let token = null;

    for (const cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'token') {
            token = value;
            break;
        }
    }
    console.log(token)
    if (token && token != "") {
        req.headers.authorization = `Bearer ${token}`
    }
    return req
})

export default api