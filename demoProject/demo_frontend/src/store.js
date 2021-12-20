import { createStore } from 'redux';


function adminReducer(state, action) {
  switch(action.type) {
    case 'login':
      return { ...state, userInfo: action.userInfo };
    case 'logout':
      return { ...state, userInfo: undefined };
    default:
      return state;
  }
}

export default createStore(adminReducer);
