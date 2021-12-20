import React, {useState} from 'react';
import './movie_info.css'
import HeaderMenu from "../component/header";
import FindingMoviesFooter from "../component/footer";
import {Modal, Rate, Descriptions, Col, Image, Row, Card, Tag, Table, Typography, Button} from "antd";
import logo from "../assets/logo.png";
import ShowMovieByType from "../component/show_movie_by_type";


export default class MovieInfoPage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            castVisible: false,
            crewVisible: false,
        };
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
        const casts = [
            {"_character": "Disappointed Man", "name": "George Lucas"},
            {"_character": "Disappointed Man", "name": "George Lucas"},
            {"_character": "Disappointed Man", "name": "George Lucas"},
            {"_character": "Disappointed Man", "name": "George Lucas"},
            {"_character": "Disappointed Man", "name": "George Lucas"},
            {"_character": "Disappointed Man", "name": "George Lucas"},
            {"_character": "Disappointed Man", "name": "George Lucas"},
        ]
        const crews = [
            {"job": "Director", "name": "George Lucas"},
            {"job": "Director", "name": "George Lucas"},
            {"job": "Director", "name": "George Lucas"},
            {"job": "Director", "name": "George Lucas"},
            {"job": "Director", "name": "George Lucas"},
            {"job": "Director", "name": "George Lucas"},
        ]
        return (
            <div className={"movie-info-container"}>
                <HeaderMenu/>
                <div className={"movie-info-content"}>
                    <Card className={"movie-info-show-card"}>
                        <Row wrap={false} align={"middle"}>
                            <Col span={6}>
                                <Image
                                    className={"movie-card-image-style"}
                                    preview={false}
                                    src={"https://m.media-amazon.com/images/M/MV5BMjI2ODE4ODAtMDA3MS00ODNkLTg4N2EtOGU0YjZmNGY4NjZlXkEyXkFqcGdeQXVyMTY5MDE5NA@@._V1_.jpg"}
                                    fallback={logo}
                                    alt={"8844"}/>
                            </Col>
                            <Col offset={1}>
                                <Descriptions className={"movie-info-show-title"} labelStyle={{color: "white"}}
                                              title="Forrest Gump" bordered>
                                    <Descriptions.Item label="adult">False</Descriptions.Item>
                                    <Descriptions.Item label="status">Released</Descriptions.Item>
                                    <Descriptions.Item label="original language">en</Descriptions.Item>

                                    <Descriptions.Item label="budget">94000000</Descriptions.Item>
                                    <Descriptions.Item label="imdb id">tt0266543</Descriptions.Item>
                                    <Descriptions.Item label="revenue">677945399</Descriptions.Item>

                                    <Descriptions.Item label="original title">Finding Nemo</Descriptions.Item>
                                    <Descriptions.Item label="popularity">25.497794</Descriptions.Item>
                                    <Descriptions.Item label="release date">2003-05-30</Descriptions.Item>
                                    <Descriptions.Item span={3}
                                                       label="homepage">http://www.starwars.com/films/star-wars-episode-iv-a-new-hope</Descriptions.Item>
                                    <Descriptions.Item span={3} label="tag line">The world will never be the same, once
                                        you've seen it through the eyes of Forrest Gump.</Descriptions.Item>
                                    <Descriptions.Item span={3} label="overview">Nemo, an adventurous young clownfish,
                                        is unexpectedly taken from his Great Barrier Reef home to a dentist's office
                                        aquarium. It's up to his worrisome father Marlin and a friendly but forgetful
                                        fish Dory to bring Nemo home -- meeting vegetarian sharks, surfer dude turtles,
                                        hypnotic jellyfish, hungry seagulls, and more along the way.</Descriptions.Item>

                                    <Descriptions.Item span={3} label="genres">
                                        <Tag color={colors[0]}>恐怖片</Tag>
                                        <Tag color={colors[1]}>恐怖片</Tag>
                                        <Tag color={colors[2]}>恐怖片</Tag>
                                        <Tag color={colors[3]}>恐怖片</Tag>
                                        <Tag color={colors[4]}>恐怖片</Tag>
                                        <Tag color={colors[5]}>恐怖片</Tag>
                                        <Tag color={colors[6]}>恐怖片</Tag>
                                        <Tag color={colors[7]}>恐怖片</Tag>
                                    </Descriptions.Item>
                                    <Descriptions.Item span={3} label="rating">
                                        <Rate allowHalf disabled={true} defaultValue={4.7}/>
                                    </Descriptions.Item>
                                    <Descriptions.Item span={3} label="extra">
                                        <Row justify={"space-around"}>
                                            <Button className={"extra-info-button"} type="primary"
                                                    onClick={() => this.openCastModel()}>Show Casts</Button>
                                            <Button className={"extra-info-button"} type="primary"
                                                    onClick={() => this.openCrewModel()}>Show Crews</Button>
                                        </Row>
                                    </Descriptions.Item>
                                </Descriptions>
                            </Col>
                        </Row>
                    </Card>
                    <ShowMovieByType/>
                </div>
                <FindingMoviesFooter/>
                <Modal title="Cast List" visible={this.state.castVisible} onOk={() => this.closeCastModel()}
                       onCancel={() => this.closeCastModel()}>
                    <Table
                        pagination={{
                            showSizeChanger: true,
                            position: ["none", "bottomCenter"],
                            total: casts.length,
                            onChange: (page, pageSize) => {
                                this.setState({pageSize: pageSize});
                            }
                        }}
                        dataSource={casts}>
                        <Table.Column title="Character" dataIndex="_character" key="_character"/>
                        <Table.Column title="Name" dataIndex="name" key="castName"/>
                    </Table>
                </Modal>
                <Modal title="Crew List" visible={this.state.crewVisible} onOk={() => this.closeCrewModel()}
                       onCancel={() => this.closeCrewModel()}>
                    <Table
                        pagination={{
                            showSizeChanger: true,
                            position: ["none", "bottomCenter"],
                            total: crews.length,
                            onChange: (page, pageSize) => {
                                this.setState({pageSize: pageSize});
                            }
                        }}
                        dataSource={crews}>
                        <Table.Column title="Job" dataIndex="job" key="job"/>
                        <Table.Column title="Name" dataIndex="name" key="crewName"/>
                    </Table>
                </Modal>
            </div>
        );
    }

}
