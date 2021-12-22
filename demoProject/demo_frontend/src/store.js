import { createStore } from 'redux';


function userReducer(state, action) {
  switch(action.type) {
    case 'login':
      return { ...state, userInfo: action.loginInfo };
    case 'logout':
      return { ...state, userInfo: undefined };
    default:
      return state;
  }
}

export default createStore(userReducer);
