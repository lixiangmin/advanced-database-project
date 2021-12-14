package advanced.database.course.demo.entity;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity
@Table(name = "cast")
public class Cast {
    private Integer castId;
    private String character;
    private String creditId;
    private Integer gender;
    private int id;
    private String name;
    private Integer order;
    private String profilePath;

    private Set<Movie> movies = new HashSet<Movie>();

    @Basic
    @Column(name = "cast_id")
    public Integer getCastId() {
        return castId;
    }

    public void setCastId(Integer castId) {
        this.castId = castId;
    }

    @Basic
    @Column(name = "_character")
    public String getCharacter() {
        return character;
    }

    public void setCharacter(String character) {
        this.character = character;
    }

    @Basic
    @Column(name = "credit_id")
    public String getCreditId() {
        return creditId;
    }

    public void setCreditId(String creditId) {
        this.creditId = creditId;
    }

    @Basic
    @Column(name = "gender")
    public Integer getGender() {
        return gender;
    }

    public void setGender(Integer gender) {
        this.gender = gender;
    }

    @Id
    @Column(name = "id")
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    @Basic
    @Column(name = "name")
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Basic
    @Column(name = "_order")
    public Integer getOrder() {
        return order;
    }

    public void setOrder(Integer order) {
        this.order = order;
    }

    @Basic
    @Column(name = "profile_path")
    public String getProfilePath() {
        return profilePath;
    }

    public void setProfilePath(String profilePath) {
        this.profilePath = profilePath;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Cast that = (Cast) o;
        return id == that.id &&
                Objects.equals(castId, that.castId) &&
                Objects.equals(character, that.character) &&
                Objects.equals(creditId, that.creditId) &&
                Objects.equals(gender, that.gender) &&
                Objects.equals(name, that.name) &&
                Objects.equals(order, that.order) &&
                Objects.equals(profilePath, that.profilePath);
    }

    @Override
    public int hashCode() {
        return Objects.hash(castId, character, creditId, gender, id, name, order, profilePath);
    }

    @JsonIgnoreProperties(value = {"casts"})
    @ManyToMany(mappedBy = "casts")
    public Set<Movie> getMovies() {
        return movies;
    }

    public void setMovies(Set<Movie> movieEntities) {
        this.movies = movieEntities;
    }
}
