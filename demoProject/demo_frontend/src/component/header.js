import React from 'react';
import {Typography, Col, Row, Image, Input} from 'antd';
import './header.css'
import logo from '../assets/logo.png'
import {Link} from "react-router-dom";
import store from "../store";

const {Search} = Input;

export default class HeaderMenu extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: undefined
        };
    }

    onSearch(key) {
        this.props.history.push({
            pathname: '/search',
            state: {
                type: "text",
                value: key
            }
        });
    }

    render() {
        return (
            <div id={"header-container"}>
                <Row id={"header-row"}>
                    <Row id={"header-content"} align={"middle"} wrap={false} justify={"space-around"}>
                        <Col span={6} id={"header-logo-title-col"}>
                            <Row align={"middle"} wrap={false}>
                                <Col>
                                    <Image width={60} height={60} wrapperClassName={"header-menu-logo-img-div"}
                                           className={"header-menu-logo-img"}
                                           src={logo} preview={false}/>
                                </Col>
                                <Col>
                                    <Link to="/home"
                                          id={"header-menu-title-text"}>FindingMovies</Link>
                                </Col>

                            </Row>
                        </Col>
                        <Col span={13}>
                            <Search
                                onSearch={(key) => {
                                    this.onSearch(key)
                                }}
                                placeholder="Enter Movie Text"/>
                        </Col>
                        <Col span={3}>
                            <Typography.Text
                                id={"header-menu-title-text"}>{store.getState() === undefined ? "visitor" : store.getState().userInfo === undefined ? "visitor" : store.getState().userInfo}</Typography.Text>
                        </Col>
                    </Row>
                </Row>
            </div>
        );
    }

}
