package advanced.database.course.demo.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity
@Table(name = "spoken_language")
public class SpokenLanguage {
    private String iso6391;
    private String name;

    private Set<Movie> movies = new HashSet<Movie>();

    @Id
    @Column(name = "iso_639_1")
    public String getIso6391() {
        return iso6391;
    }

    public void setIso6391(String iso6391) {
        this.iso6391 = iso6391;
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
        SpokenLanguage that = (SpokenLanguage) o;
        return Objects.equals(iso6391, that.iso6391) &&
                Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(iso6391, name);
    }

    @JsonIgnore
    @ManyToMany(mappedBy = "spokenLanguages")
    public Set<Movie> getMovies() {
        return movies;
    }

    public void setMovies(Set<Movie> movies) {
        this.movies = movies;
    }
}
