import React, {useState} from 'react';
import './movie_info.css'
import HeaderMenu from "../component/header";
import FindingMoviesFooter from "../component/footer";
import {Modal, Rate, Descriptions, Col, Image, Row, Card, Tag, Table, Typography, Button, Space} from "antd";
import logo from "../assets/logo.png";
import {
    findMovieById,
    findTheCastsOfMovie,
    findTheCrewsOfMovie,
    findTheRecommendsOfMovie,
    findTheTypesOfMovie
} from "../request";
import ShowMovieByType from "../component/show_movie_by_type";
import store from "../store";

export default class MovieInfoPage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            movie: {},
            types: [],
            crews: [],
            casts: [],
            recommends: [],
            castVisible: false,
            crewVisible: false,
            rateVisible: false,
            id: this.props.match.params.id
        };
    }

    componentDidUpdate(prevProps) {
        // 典型用法（不要忘记比较 props）：
        if (this.props.match.params.id !== prevProps.match.params.id) {
            this.setState({
                id: this.props.match.params.id
            }, () => {
                this.getData()
            });
        }
    }

    componentDidMount() {
        this.getData();
    }

    getData() {
        this.getMovieById();
        this.getTypesById();
        this.getCrewsById();
        this.getCastsById();
        this.getRecommendsById();
    }

    getMovieById() {
        findMovieById(this.state.id, {
            successCb: resp => {
                this.setState({
                    movie: resp.movie
                });
            }
        })
    }

    getTypesById() {
        findTheTypesOfMovie({id: this.state.id},
            {
                successCb: resp => {
                    this.setState({
                        types: resp.types
                    });
                }
            })
    }

    getCastsById() {
        findTheCastsOfMovie({id: this.state.id},
            {
                successCb: resp => {
                    this.setState({
                        casts: resp.casts
                    });
                }
            })
    }

    getCrewsById() {
        findTheCrewsOfMovie({id: this.state.id},
            {
                successCb: resp => {
                    this.setState({
                        crews: resp.crews
                    });
                }
            })
    }

    getRecommendsById() {
        findTheRecommendsOfMovie(this.state.id, {
            successCb: resp => {
                this.setState({
                    recommends: resp.recommends
                });
            }
        })
    }

    openRateModel() {
        this.setState({
            rateVisible: true
        })
    }

    closeRateModel() {
        this.setState({
            rateVisible: false
        })
    }

    openCrewModel() {
        this.setState({
            crewVisible: true
        })
    }

    closeCrewModel() {
        this.setState({
            crewVisible: false
        })
    }

    closeCastModel() {
        this.setState({
            castVisible: false
        })
    }

    openCastModel() {
        this.setState({
            castVisible: true
        })
    }

    render() {
        const colors = ["magenta", "red", "volcano", "orange", "gold", "lime", "green", "cyan", "blue", "geekblue", "purple"]
        return (
            <div className={"movie-info-container"}>
                <HeaderMenu history={this.props.history}/>
                <div className={"movie-info-content"}>
                    <Card className={"movie-info-show-card"}>
                        <Row wrap={false} align={"middle"}>
                            <Col span={6}>
                                <Image
                                    className={"movie-card-image-style"}
                                    preview={false}
                                    src={this.state.movie.posterPath}
                                    fallback={logo}
                                    alt={this.state.movie.title}/>
                            </Col>
                            <Col offset={1}>
                                <Descriptions className={"movie-info-show-title"} labelStyle={{color: "white"}}
                                              title={this.state.movie.title} bordered>
                                    <Descriptions.Item label="adult">{this.state.movie.adult}</Descriptions.Item>
                                    <Descriptions.Item label="status">{this.state.movie.status}</Descriptions.Item>
                                    <Descriptions.Item
                                        label="original language">{this.state.movie.originalLanguage}</Descriptions.Item>

                                    <Descriptions.Item label="budget">{this.state.movie.budget}</Descriptions.Item>
                                    <Descriptions.Item label="imdb id">{this.state.movie.imdbId}</Descriptions.Item>
                                    <Descriptions.Item label="revenue">{this.state.movie.revenue}</Descriptions.Item>

                                    <Descriptions.Item
                                        label="original title">{this.state.movie.originalTitle}</Descriptions.Item>
                                    <Descriptions.Item
                                        label="popularity">{this.state.movie.popularity}</Descriptions.Item>
                                    <Descriptions.Item
                                        label="release date">{this.state.movie.releaseDate}</Descriptions.Item>
                                    <Descriptions.Item span={3}
                                                       label="homepage">{this.state.movie.homepage}</Descriptions.Item>
                                    <Descriptions.Item span={3}
                                                       label="tag line">{this.state.movie.tagline}</Descriptions.Item>
                                    <Descriptions.Item span={3}
                                                       label="overview">{this.state.movie.overview}</Descriptions.Item>

                                    <Descriptions.Item span={3} label="genres">
                                        {this.state.types.map((item, i) => {
                                            let index = i
                                            if (i >= colors.length) {
                                                index = i % colors.length
                                            }
                                            return <Tag color={colors[index]}>{item.name}</Tag>
                                        })
                                        }
                                    </Descriptions.Item>
                                    <Descriptions.Item span={3} label="rating">
                                        <Rate allowHalf disabled={true} value={this.state.movie.score}/>
                                    </Descriptions.Item>
                                    <Descriptions.Item span={3} label="extra">
                                        <Row justify={"space-around"}>
                                            <Button className={"extra-info-button"} type="primary"
                                                    onClick={() => this.openCastModel()}>Show Casts</Button>
                                            {store.getState() !== undefined && store.getState().userInfo !== undefined ?
                                                <Button className={"extra-info-button"} type="primary"
                                                        onClick={() => this.openRateModel()}>Rate Movie</Button>
                                            :<div/>}
                                            <Button className={"extra-info-button"} type="primary"
                                                    onClick={() => this.openCrewModel()}>Show Crews</Button>
                                        </Row>
                                    </Descriptions.Item>
                                </Descriptions>
                            </Col>
                        </Row>
                    </Card>
                    {
                        this.state.recommends.length > 0 ? <Card className={"movie-info-show-card"}>
                            <ShowMovieByType id={this.state.id} type={"Recommends"} history={this.props.history}
                                             movies={this.state.recommends}/>
                        </Card> : <div/>
                    }
                </div>
                <FindingMoviesFooter/>
                <Modal title="Cast List" visible={this.state.castVisible}
                       onOk={() => this.closeCastModel()}
                       onCancel={() => this.closeCastModel()}>
                    <Table
                        scroll={{y: 550}}
                        pagination={{
                            hideOnSinglePage: true,
                            showSizeChanger: true,
                            position: ["none", "bottomCenter"],
                            total: this.state.casts.length,
                            onChange: (page, pageSize) => {
                                this.setState({pageSize: pageSize});
                            }
                        }}
                        dataSource={this.state.casts}>
                        <Table.Column title="Character" dataIndex="character" key="character"/>
                        <Table.Column title="Name" dataIndex="name" key="castName"/>
                    </Table>
                </Modal>
                <Modal title="Crew List" visible={this.state.crewVisible}
                       onOk={() => this.closeCrewModel()}
                       onCancel={() => this.closeCrewModel()}>
                    <Table
                        scroll={{y: 550}}
                        pagination={{
                            hideOnSinglePage: true,
                            showSizeChanger: true,
                            position: ["none", "bottomCenter"],
                            total: this.state.crews.length,
                            onChange: (page, pageSize) => {
                                this.setState({pageSize: pageSize});
                            }
                        }}
                        dataSource={this.state.crews}>
                        <Table.Column title="Department" dataIndex="department" key="department"/>
                        <Table.Column title="Job" dataIndex="job" key="job"/>
                        <Table.Column title="Name" dataIndex="name" key="crewName"/>
                    </Table>
                </Modal>
                <Modal width={300} title="Rate Panel" visible={this.state.rateVisible}
                       onOk={() => this.closeRateModel()}
                       onCancel={() => this.closeRateModel()}>
                    <Space direction={"vertical"} align={"center"}>
                        <Typography.Text>Tell Your Feeling About This Movie.</Typography.Text>
                        <Rate allowHalf/>
                    </Space>
                </Modal>
            </div>
        );
    }
}
