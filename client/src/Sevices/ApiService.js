import axios from "axios";
import ApiUrl from "../ServerApi";

const USER_API_BASE_URL = `${ApiUrl}/experiments`;

class ApiService {
  fetchUsers() {
    return axios.get(USER_API_BASE_URL);
  }

  fetchUserById(userId) {
    return axios.get(USER_API_BASE_URL + "/" + userId);
  }

  deleteUser(userId) {
    return axios.delete(USER_API_BASE_URL + "/" + userId);
  }

  addUser(user) {
    return axios.post("" + USER_API_BASE_URL, user);
  }

  editUser(user) {
    return axios.patch(USER_API_BASE_URL + "/" + user._id, user);
  }
}

export default new ApiService();
