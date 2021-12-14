package advanced.database.course.demo.entity;

import javax.persistence.*;
import java.util.Objects;

@Entity
@Table(name = "link")
public class Link {
    private int id;
    private Integer imdbId;
    private Integer tmdbId;

    @Id
    @Column(name = "id")
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    @Basic
    @Column(name = "imdb_id")
    public Integer getImdbId() {
        return imdbId;
    }

    public void setImdbId(Integer imdbId) {
        this.imdbId = imdbId;
    }

    @Basic
    @Column(name = "tmdb_id")
    public Integer getTmdbId() {
        return tmdbId;
    }

    public void setTmdbId(Integer tmdbId) {
        this.tmdbId = tmdbId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Link that = (Link) o;
        return id == that.id &&
                Objects.equals(imdbId, that.imdbId) &&
                Objects.equals(tmdbId, that.tmdbId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, imdbId, tmdbId);
    }
}
