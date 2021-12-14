package advanced.database.course.demo.entity;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity
@Table(name = "production_country")
public class ProductionCountry {
    private String iso31661;
    private String name;

    private Set<Movie> movies = new HashSet<Movie>();

    @Id
    @Column(name = "iso_3166_1")
    public String getIso31661() {
        return iso31661;
    }

    public void setIso31661(String iso31661) {
        this.iso31661 = iso31661;
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
        ProductionCountry that = (ProductionCountry) o;
        return Objects.equals(iso31661, that.iso31661) &&
                Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(iso31661, name);
    }

    @JsonIgnoreProperties(value = {"productionCountries"})
    @ManyToMany(mappedBy = "productionCountries")
    public Set<Movie> getMovies() {
        return movies;
    }

    public void setMovies(Set<Movie> movies) {
        this.movies = movies;
    }
}
