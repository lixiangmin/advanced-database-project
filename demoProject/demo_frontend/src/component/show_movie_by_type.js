import React from 'react';
import {List, Typography, Col, Row, Card} from 'antd';
import './show_movie_by_type.css'
import MovieCard from "./movie_card";

export default class ShowMovieByType extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    generateMovies(movies) {
        return movies.map((item, i) => {
            return <Col span={3}>
                <MovieCard history={this.props.history}
                           id={item.id}
                           poster={item.posterPath}
                           title={item.title}
                           releaseDate={item.releaseDate}/></Col>
        });
    }

    moreOnClick() {
        this.props.history.push({
            pathname: '/search',
            state: {
                type: this.props.type === "Recommends" ? "recommends" : "type",
                value: this.props.id
            }
        });
    }

    render() {
        return (
            <div className={"movies-show-container"}>
                <Row className={"movies-type-show-row"} wrap={false} align={"space-between"}>
                    <Typography.Text className={"movies-type"}>{this.props.type}</Typography.Text>
                    <Typography.Link onClick={() => this.moreOnClick()}
                                     className={"movies-show-more-link"}>more</Typography.Link>
                </Row>
                <Row wrap={false} align={"space-between"}>
                    {this.generateMovies(this.props.movies)}
                </Row>
            </div>
        );
    }

}
