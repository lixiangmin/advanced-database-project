package advanced.database.course.demo.entity;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity
@Table(name = "keyword")
public class Keyword {
    private int id;
    private String name;

    private Set<Movie> movies = new HashSet<Movie>();

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

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Keyword that = (Keyword) o;
        return id == that.id &&
                Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name);
    }

    @JsonIgnoreProperties(value = {"keywords"})
    @ManyToMany(mappedBy = "keywords")
    public Set<Movie> getMovies() {
        return movies;
    }

    public void setMovies(Set<Movie> movieEntities) {
        this.movies = movieEntities;
    }
}
