package advanced.database.course.demo.entity;

import javax.persistence.*;
import java.util.Objects;

@Entity
@Table(name = "rating")
public class Rating {
    private Double score;
    private Long timestamp;
    private int ratingId;
    private int userId;
    private int movieId;

    @Basic
    @Column(name = "score")
    public Double getScore() {
        return score;
    }

    public void setScore(Double rating) {
        this.score = rating;
    }

    @Basic
    @Column(name = "timestamp")
    public Long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(Long timestamp) {
        this.timestamp = timestamp;
    }

    @Id
    @Column(name = "rating_id")
    public int getRatingId() {
        return ratingId;
    }

    public void setRatingId(int ratingId) {
        this.ratingId = ratingId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Rating that = (Rating) o;
        return ratingId == that.ratingId &&
                Objects.equals(score, that.score) &&
                Objects.equals(timestamp, that.timestamp);
    }

    @Override
    public int hashCode() {
        return Objects.hash(score, timestamp, ratingId);
    }

    @Basic
    @Column(name = "movie_id")
    public int getMovieId() {
        return movieId;
    }

    public void setMovieId(int movieId) {
        this.movieId = movieId;
    }

    @Basic
    @Column(name = "user_id")
    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }
}
