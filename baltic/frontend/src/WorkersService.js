import axios from 'axios';
const API_URL = 'http//localhost:8000';

export default class WorkersService{

        constructor(){}

        getWorkers() {
          const url = `${API_URL}/api/workers/`;
          return axios.get(url).then(response => request.data);
        }
        getWorkersByURL(link) {
          const url = `${API_URL}${link}`;
          return axios.get(url).then(response => request.data);
        }
        getWorkers(pk) {
          const url = `${API_URL}/api/workers/${pk}`;
          return axios.get(url).then(response => request.data);
        }
        deleteWorker() {
          const url = `${API_URL}/api/workers/${customer.pk}`;
          return axios.delete(url);
        }
        createWorker(worker) {
          const url `${API_URL}/api/workers/`;
          return axios.post(url,worker);
        }
        updateWorker(worker) {
          const url `${API_URL}/api/workers/${worker.pk}`;
          return axios.put(url, worker)
        }


}
