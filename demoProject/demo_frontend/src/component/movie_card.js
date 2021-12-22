import React from 'react';
import {Image, Card, Button} from 'antd';
import Meta from "antd/es/card/Meta";
import logo from "../assets/logo.png"
import {Link} from 'react-router-dom';

export default class MovieCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    // moreInfoClick() {
    //     this.props.history.push({
    //         pathname: "/movieInfo",
    //         state: {
    //             id: this.props.id
    //         }
    //     });
    // }


    render() {
        return (
            <Card
                actions={[
                    <Link to={`/movieInfo/${this.props.id}`}>
                        <Button block type="link">
                            More Information
                        </Button></Link>
                ]}
                cover={<Image
                    preview={false}
                    src={this.props.poster === undefined || this.props.poster === null ? "error" : this.props.poster}
                    fallback={logo}
                    alt={this.props.title}/>}
            >
                <Meta title={this.props.title} description={this.props.releaseDate}/>
            </Card>
        );
    }

}
