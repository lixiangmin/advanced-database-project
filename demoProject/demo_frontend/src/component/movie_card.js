import React from 'react';
import {Image, Card, Button} from 'antd';
import Meta from "antd/es/card/Meta";
import logo from "../assets/logo.png"

export default class MovieCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }


    render() {
        return (
            <Card
                actions={[
                    <Button type="primary">
                        More Information
                    </Button>
                ]}
                cover={<Image
                    preview={false}
                    src={this.props.poster}
                    fallback={logo}
                    alt={this.props.title}/>}
            >
                <Meta title={this.props.title} description={this.props.description}/>
            </Card>
        );
    }

}
