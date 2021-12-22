import React from 'react';
import {Form, Input, Button, message} from 'antd';
import './login.css'
import store from '../store';
import {userLogin} from '../request';
import FindingMoviesFooter from "../component/footer";

export default class LoginPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: ""
        };
    }

    login(values) {
        userLogin(values, {
            successCb: resp => {
                store.dispatch({
                    type: "login",
                    loginInfo: this.state.username
                });
                this.setState({loginLoading: false});
                message.success(resp.msg)
                this.props.history.push("/home");
            },
            failCb: msg => {
                this.setState({loginLoading: false});
                message.error(msg);
            }
        });
    }

    visit() {
        this.props.history.push("/home");
    }

    handleChange(e) {
        this.setState({
            username: e.target.value
        })
    }

    render() {
        return (
            <div className={"login-container"}>
                <div className={"login-box"}>
                    <h2>FindingMovies</h2>
                    <Form>
                        <Form.Item>
                            <div className={"login-field"}>
                                <Input
                                    type="text" onChange={this.handleChange.bind(this)}
                                    defaultValue={this.state.username}/>
                                <label>username</label>
                            </div>
                        </Form.Item>
                        <Form.Item>
                            <Button type="primary"
                                    onClick={() => {
                                        this.login({username: this.state.username})
                                    }}>Login</Button>
                        </Form.Item>
                        <Form.Item>
                            <Button type="primary"
                                    onClick={() => {
                                        this.visit()
                                    }}>Visit</Button>
                        </Form.Item>
                    </Form>
                </div>
                <div id={"login-footer"}>
                    <FindingMoviesFooter/>
                </div>
            </div>
        );
    }

}
