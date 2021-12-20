import React from 'react';
import {Card, Carousel, Col, Row, Typography} from 'antd';
import {LeftCircleOutlined, RightCircleOutlined} from '@ant-design/icons';
import './home.css'
import HeaderMenu from "../component/header";
import ShowMovieByType from "../component/show_movie_by_type";
import MovieCard from "../component/movie_card";
import FindingMoviesFooter from "../component/footer";

export default class HomePage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        };
        this.next = this.next.bind(this);
        this.prev = this.prev.bind(this);
    }

    next() {
        this.slider.next();
    }

    prev() {
        this.slider.prev();
    }

    render() {
        return (
            <div className={"home-container"}>
                <HeaderMenu/>
                <div className={"home-content"}>
                    <Card id={"recommend-movie-card"} type="inner">
                        <Typography.Text id={"recommend-movie-title"}>Recommended Movies</Typography.Text>
                        <div id={"recommend-movie-show-div"}>
                            <Carousel dots={false} autoplay={true} ref={el => (this.slider = el)}>
                                <div>
                                    <Row wrap={false} align={"space-between"}>
                                        <Col span={6}>
                                            <MovieCard
                                                poster="https://m.media-amazon.com/images/M/MV5BYzJkYmQ3ZTQtYmMwZS00YTdjLTkwMTEtYTQ5NzcxMjA0ZjkwXkEyXkFqcGdeQXVyNjY5MDUyMjE@._V1_.jpg"
                                                title="test"
                                                description="this is a test"/>
                                        </Col>
                                        <Col offset={3} span={6}>
                                            <MovieCard
                                                poster="https://m.media-amazon.com/images/M/MV5BMTQyODc3MTQzMF5BMl5BanBnXkFtZTcwMjg2MTQyMQ@@._V1_.jpg"
                                                title="test"
                                                description="this is a test"/>
                                        </Col>
                                        <Col offset={3} span={6}>
                                            <MovieCard
                                                poster="https://m.media-amazon.com/images/M/MV5BMTI2OTQ0MjAyNV5BMl5BanBnXkFtZTcwNjAzOTA4MQ@@._V1_.jpg"
                                                title="test"
                                                description="this is a test"/>
                                        </Col>
                                    </Row>
                                </div>
                                <div>
                                    <Row wrap={false} align={"space-between"}>
                                        <Col span={6}>
                                            <MovieCard
                                                poster="https://m.media-amazon.com/images/M/MV5BMTcyNTQ3ODY1OF5BMl5BanBnXkFtZTcwMzc2MDg5MQ@@._V1_.jpg"
                                                title="test"
                                                description="this is a test"/>
                                        </Col>
                                        <Col offset={3} span={6}>
                                            <MovieCard
                                                poster="https://m.media-amazon.com/images/M/MV5BMzg1OTA1YWYtZjRlNy00MDk3LTg1NjctZTgzZGVmYjgzYzRjXkEyXkFqcGdeQXVyMjUxODE0MDY@._V1_.jpg"
                                                title="test"
                                                description="this is a test"/>
                                        </Col>
                                        <Col offset={3} span={6}>
                                            <MovieCard
                                                poster="https://m.media-amazon.com/images/M/MV5BMGM3YWMyODQtMTJhZC00NmVmLWFhMmQtZGY4ZjMxZDcxOTA1XkEyXkFqcGdeQXVyMzM4MjM0Nzg@._V1_.jpg"
                                                title="test"
                                                description="this is a test"/>
                                        </Col>
                                    </Row>
                                </div>
                                <div>
                                    <Row wrap={false} align={"space-between"}>
                                        <Col span={6}>
                                            <MovieCard
                                                poster="https://m.media-amazon.com/images/M/MV5BYTZhNmMwOWEtMzFmYS00ODFlLWFmZjMtM2Q5M2ZlYjgwNzU2XkEyXkFqcGdeQXVyNzI1NzMxNzM@._V1_.jpg"
                                                title="test"
                                                description="this is a test"/>
                                        </Col>
                                        <Col offset={3} span={6}>
                                            <MovieCard
                                                poster="https://m.media-amazon.com/images/M/MV5BMjgzMTgwNTI1M15BMl5BanBnXkFtZTgwMTgxNjk3MjE@._V1_.jpg"
                                                title="test"
                                                description="this is a test"/>
                                        </Col>
                                        <Col offset={3} span={6}>
                                            <MovieCard
                                                poster="https://m.media-amazon.com/images/M/MV5BMjAwOTM2MzE5MF5BMl5BanBnXkFtZTcwMjM0NTcyMg@@._V1_.jpg"
                                                title="test"
                                                description="this is a test"/>
                                        </Col>
                                    </Row>
                                </div>
                            </Carousel>
                        </div>
                        <LeftCircleOutlined id={"recommend-movie-show-prev"} onClick={this.prev}/>
                        <RightCircleOutlined id={"recommend-movie-show-next"} onClick={this.next}/>
                    </Card>
                    <ShowMovieByType/>
                </div>
                <FindingMoviesFooter/>
            </div>
        );
    }

}
