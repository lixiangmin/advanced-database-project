import React from 'react';
import {Tabs, Card, Carousel, Col, message, Row, Typography} from 'antd';
import {LeftCircleOutlined, RightCircleOutlined} from '@ant-design/icons';
import './home.css'
import HeaderMenu from "../component/header";
import ShowMovieByType from "../component/show_movie_by_type";
import MovieCard from "../component/movie_card";
import FindingMoviesFooter from "../component/footer";
import {moviesWithType, movieTypes, recommendMovies} from "../request";

export default class HomePage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            recommendMovies: [],
            moviesWithType: [],
            types: [],
            selectedType: undefined
        };
        this.next = this.next.bind(this);
        this.prev = this.prev.bind(this);
    }

    componentDidMount() {
        this.getRecommendMovies();
        this.getMovieTypes();
    }

    getRecommendMovies() {
        recommendMovies({
            successCb: resp => {
                this.setState({
                    recommendMovies: resp.movies
                });
            }
        });
    }

    getMoviesWithType() {
        moviesWithType({type: this.state.selectedType}, {
            successCb: resp => {
                this.setState({
                    moviesWithType: resp.movies
                });
            }
        });
    }

    getMovieTypes() {
        movieTypes({
            successCb: resp => {
                this.setState({
                    types: resp.genres,
                    selectedType: resp.genres[0].name
                }, function () {
                    this.getMoviesWithType();
                });
            }
        });
    }

    next() {
        this.slider.next();
    }

    prev() {
        this.slider.prev();
    }

    generateRecommendMovies(recommendMovies) {
        let movieGroupNum = recommendMovies.length / 3
        let movieGroup = []
        for (let i = 0; i < movieGroupNum; i++) {
            movieGroup.push([recommendMovies[3 * i], recommendMovies[3 * i + 1], recommendMovies[3 * i + 2]])
        }
        return movieGroup.map((item, i) => {
            return (
                <React.Fragment>
                    <div>
                        <Row wrap={false} align={"space-between"}>
                            <Col span={6}>
                                <MovieCard history={this.props.history}
                                           id={item[0].id}
                                           poster={item[0].posterPath}
                                           title={item[0].title}
                                           releaseDate={item[0].releaseDate}/>
                            </Col>
                            <Col offset={3} span={6}>
                                <MovieCard history={this.props.history}
                                           id={item[1].id}
                                           poster={item[1].posterPath}
                                           title={item[1].title}
                                           releaseDate={item[1].releaseDate}/>
                            </Col>
                            <Col offset={3} span={6}>
                                <MovieCard history={this.props.history}
                                           id={item[2].id}
                                           poster={item[2].posterPath}
                                           title={item[2].title}
                                           releaseDate={item[2].releaseDate}/>
                            </Col>
                        </Row>
                    </div>
                </React.Fragment>
            )
        });
    }

    generateTypes(types) {
        return types.map((type, i) => {
            return (<Tabs.TabPane tab={type.name} key={type.name}>
                {<ShowMovieByType id={type.id} history={this.props.history}
                                  type={type.name} movies={this.state.moviesWithType}/>}
            </Tabs.TabPane>)
        });
    }

    typeChange(key) {
        this.setState({
            selectedType: key
        }, function () {
            this.getMoviesWithType();
        });
    }


    render() {
        return (
            <div className={"home-container"}>
                <HeaderMenu history={this.props.history}/>
                <div className={"home-content"}>
                    <Card id={"recommend-movie-card"} type="inner">
                        <Typography.Text id={"recommend-movie-title"}>Recommended Movies</Typography.Text>
                        <div id={"recommend-movie-show-div"}>
                            <Carousel dots={false} autoplay={true} ref={el => (this.slider = el)}>
                                {this.generateRecommendMovies(this.state.recommendMovies)}
                            </Carousel>
                        </div>
                        <LeftCircleOutlined id={"recommend-movie-show-prev"} onClick={this.prev}/>
                        <RightCircleOutlined id={"recommend-movie-show-next"} onClick={this.next}/>
                    </Card>

                    <Card className={"movies-type-show-card"}>
                        <Tabs onChange={(key) => this.typeChange(key)} id={"movie-type-show-tab"}>
                            {this.generateTypes(this.state.types)}
                        </Tabs>
                    </Card>

                </div>
                <FindingMoviesFooter/>
            </div>
        );
    }

}
