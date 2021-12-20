import React from 'react';
import {Typography, Col, Row, Image, Space, Card} from 'antd';
import './show_movie_by_type.css'
import MovieCard from "./movie_card";

export default class ShowMovieByType extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }


    render() {
        return (
            <div className={"movies-show-container"}>
                <Card className={"movies-type-show-card"}>
                    <Row className={"movies-type-show-row"} wrap={false} align={"space-between"}>
                        <Typography.Text className={"movies-type"}>恐怖片</Typography.Text>
                        <Typography.Link className={"movies-show-more-link"}>more</Typography.Link>
                    </Row>
                    <Row wrap={false} align={"space-between"}>
                        <Col span={3}>
                            <MovieCard
                                poster="https://m.media-amazon.com/images/M/MV5BMjA3OTMwNTUxMl5BMl5BanBnXkFtZTgwNTkxMDkwMzE@._V1_.jpg"
                                title="test"
                                description="this is a test"/>
                        </Col>
                        <Col span={3}>
                            <MovieCard
                                poster="https://m.media-amazon.com/images/M/MV5BYWI4YzNkZDYtZTgxZS00MzU4LWE3NjYtNzEwMDBmZWQzZmE4XkEyXkFqcGdeQXVyNDc2NjEyMw@@._V1_.jpg"
                                title="test"
                                description="this is a test"/>
                        </Col>
                        <Col span={3}>
                            <MovieCard
                                poster="https://m.media-amazon.com/images/M/MV5BMTM0MDUyMzk1Ml5BMl5BanBnXkFtZTcwMjczMDU2Mg@@._V1_.jpg"
                                title="test"
                                description="this is a test"/>
                        </Col>
                        <Col span={3}>
                            <MovieCard
                                poster="https://m.media-amazon.com/images/M/MV5BMjA3YTRjMDktMDFiNC00OTg0LWI5MWMtNTFjM2ZlOTVmYmMyXkEyXkFqcGdeQXVyMjQwMjk0NjI@._V1_.jpg"
                                title="test"
                                description="this is a test"/>
                        </Col>
                        <Col span={3}>
                            <MovieCard
                                poster="https://m.media-amazon.com/images/M/MV5BMDgzYjQwMDMtNGUzYi00MTRmLWIyMGMtNjE1OGZkNzY2YWIzL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"
                                title="test"
                                description="this is a test"/>
                        </Col>
                        <Col span={3}>
                            <MovieCard
                                poster="https://m.media-amazon.com/images/M/MV5BMTMwOTg5MDk1NV5BMl5BanBnXkFtZTcwOTA0NzI5NA@@._V1_.jpg"
                                title="test"
                                description="this is a test"/>
                        </Col>
                    </Row>
                </Card>
            </div>
        );
    }

}
