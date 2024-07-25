import axios, { type AxiosInstance } from 'axios'

const api_client: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-type': 'application/json'
  }
})

export default api_client
