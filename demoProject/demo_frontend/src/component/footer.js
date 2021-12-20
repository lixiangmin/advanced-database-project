import React from 'react';
import {Typography, Col, Row, Image, Input, Divider} from 'antd';
import './footer.css'

export default class FindingMoviesFooter extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }


    render() {
        return (
            <div className={"footer-div"}>
                <Typography.Text className={"footer-info-text"}>Finding Movies ©2021 Created by Group
                    7</Typography.Text>
            </div>
        );
    }

}
