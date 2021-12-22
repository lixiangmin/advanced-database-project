import React from 'react';
import {List, Form, Input, Button, message, Card, Typography, Image, Space, Row, Col} from 'antd';
import './search.css'
import FindingMoviesFooter from "../component/footer";
import HeaderMenu from "../component/header";
import {findMovieList, findMovieListByText, findMovieListByGenreId, findMovieListByMovieId} from "../request";
import {Link} from "react-router-dom";
import logo from "../assets/logo.png";

export default class SearchPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            movies: [],
            total: 0,
            searchType: this.props.location.state.type,
            searchValue: this.props.location.state.value,
        };
    }

    componentDidUpdate(prevProps) {
        // 典型用法（不要忘记比较 props）：
        if (this.props.location.state.value !== prevProps.location.state.value || this.props.location.state.type !== prevProps.location.state.type) {
            this.setState({
                searchType: this.props.location.state.type,
                searchValue: this.props.location.state.value
            }, () => {
                this.updateList(0, 10)
            });
        }
    }

    componentDidMount() {
        this.updateList(0, 10)
    }

    getMovieList(page, size) {
        findMovieList({
            page: page,
            size: size,
        }, {
            successCb: resp => {
                this.setState({
                    movies: resp.movies,
                    total: resp.total
                });
            }
        });
    }

    getMovieListByText(page, size) {
        findMovieListByText({
            text: this.state.searchValue,
            page: page,
            size: size,
        }, {
            successCb: resp => {
                this.setState({
                    movies: resp.movies,
                    total: resp.total
                });
            }
        });
    }

    getMovieListByGenreId(page, size) {
        findMovieListByGenreId({
            genreId: this.state.searchValue,
            page: page,
            size: size,
        }, {
            successCb: resp => {
                this.setState({
                    movies: resp.movies,
                    total: resp.total
                });
            }
        });
    }

    getMovieListByMovieId(page, size) {
        findMovieListByMovieId({
            movieId: this.state.searchValue,
            page: page,
            size: size,
        }, {
            successCb: resp => {
                this.setState({
                    movies: resp.movies,
                    total: resp.total
                });
            }
        });
    }

    updateList(page, pageSize) {
        if (this.state.searchValue === null || this.state.searchValue === "" || this.state.searchValue === undefined) {
            this.getMovieList(page, pageSize);
        } else if (this.state.searchType === "text") {
            this.getMovieListByText(page, pageSize);
        } else if (this.state.searchType === "type") {
            this.getMovieListByGenreId(page, pageSize)
        } else if (this.state.searchType === "recommends") {
            this.getMovieListByMovieId(page, pageSize)
        }
    }

    render() {
        return (
            <div className={"search-movies-container"}>
                <HeaderMenu history={this.props.history}/>
                <div className={"search-movies-content"}>
                    <Card type="inner" className={"search-movies-show-card"}>
                        <Typography.Text id={"search-movies-show-title"}>Search Movies</Typography.Text>
                        <List
                            size="large"
                            pagination={{
                                hideOnSinglePage: true,
                                showSizeChanger: true,
                                total: this.state.total,
                                onChange: (page, pageSize) => {
                                    this.updateList(page - 1, pageSize)
                                }
                            }}
                            dataSource={this.state.movies}
                            renderItem={item => (
                                <List.Item
                                    key={item.id}>
                                    <Row align={"middle"}>
                                        <Col span={4}>
                                            <Image
                                                preview={false}
                                                src={item.posterPath === undefined || item.posterPath === null ? "error" : item.posterPath}
                                                fallback={logo}
                                                alt={item.title}/>
                                        </Col>
                                        <Col offset={2} span={18}>
                                            <Space direction={"vertical"} align={"center"} size={30}>
                                                <Typography.Text className={"search-movie-info-show-title"}><Link
                                                    to={`/movieInfo/${item.id}`}>{item.title}</Link></Typography.Text>
                                                <Typography.Text
                                                    className={"search-movie-info-show-content"}>{item.overview}</Typography.Text>
                                                <Link to={`/movieInfo/${item.id}`}>
                                                    <Button type={"primary"}>
                                                        More Information
                                                    </Button></Link>
                                            </Space>
                                        </Col>
                                    </Row>
                                </List.Item>
                            )}
                        />
                    </Card>
                </div>
                <FindingMoviesFooter/>
            </div>
        );
    }
}
