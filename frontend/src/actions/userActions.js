import axios from "axios";
import {
  USER_LOGIN_REQUEST,
  USER_LOGIN_SUSSESS,
  USER_LOGIN_FAIL,
  USER_LOGOUT,
  USER_REGISTER_REQUEST,
  USER_REGISTER_SUSSESS,
  USER_REGISTER_FAIL,
  USER_DETAILS_REQUEST,
  USER_DETAILS_SUSSESS,
  USER_DETAILS_FAIL,
  USER_DETAILS_RESET,
  USER_UPDATE_PROFILE_REQUEST,
  USER_UPDATE_PROFILE_SUSSESS,
  USER_UPDATE_PROFILE_FAIL,
  USER_UPDATE_PROFILE_RESET,
} from "../constants/userConstants";

export const login = (email, password) => async (dispatch) => {
  try {
    dispatch({
      type: USER_LOGIN_REQUEST,
    });

    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    const { data } = await axios.post(
      "/api/users/login/",
      {
        'username': email,
        'password': password,
      },
      config
    );
    dispatch({
      type: USER_LOGIN_SUSSESS,
      payload: data,
    });

    localStorage.setItem("userInfo", JSON.stringify(data));
    
  } catch (error) {
    dispatch({
      type: USER_LOGIN_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const logout = () => (dispatch) => {
  localStorage.removeItem("userInfo");
  dispatch({ type: USER_LOGOUT });
  dispatch({ type: USER_DETAILS_RESET });
};

export const register = (name, email, password) => async (dispatch) => {
  try {
    dispatch({
      type: USER_REGISTER_REQUEST,
    });

    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    const { data } = await axios.post(
      "/api/users/register/",
      { name: name, email: email, password: password },
      config
    );
    dispatch({
      type: USER_REGISTER_SUSSESS,
      payload: data,
    });

    dispatch({
      type: USER_LOGIN_SUSSESS,
      payload: data,
    });

    localStorage.setItem("userInfo", JSON.stringify(data));
  } catch (error) {
    dispatch({
      type: USER_REGISTER_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const getUserDetails = (id) => async (dispatch, getState) => {
  try {
    dispatch({
      type: USER_DETAILS_REQUEST,
    });

    const {
      userLogin: { userInfo }, //將userLogin中的access token 加入
    } = getState();

    const config = {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${userInfo.access}`, //將access token 加入header中，以便API發出時能夠驗證是否登入成功。
      },
    };

    const { data } = await axios.get(
      `/api/users/${id}/`, 
      config);

    dispatch({
      type: USER_DETAILS_SUSSESS,
      payload: data,
    });

  } catch (error) {
    dispatch({
      type: USER_DETAILS_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const updateUserProfile = (user) => async (dispatch, getState) => {
  try {
    dispatch({
      type: USER_UPDATE_PROFILE_REQUEST,
    });

    const {
      userLogin: { userInfo }, //將userLogin中的access token 加入
    } = getState();

    const config = {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${userInfo.access}`, //將access token 加入header中，以便API發出時能夠驗證是否登入成功。
      },
    };

    const { data } = await axios.put(
      `/api/users/profile/update/`, 
      user, 
      config);

    dispatch({
      type: USER_UPDATE_PROFILE_SUSSESS,
      payload: data,
    });
    dispatch({
      type: USER_LOGIN_SUSSESS,
      payload: data,
    });

    localStorage.setItem("userInfo", JSON.stringify(data));

  } catch (error) {
    dispatch({
      type: USER_DETAILS_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};
