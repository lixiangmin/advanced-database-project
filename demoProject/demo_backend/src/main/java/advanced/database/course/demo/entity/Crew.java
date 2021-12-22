package advanced.database.course.demo.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity
@Table(name = "crew")
public class Crew {
    private String creditId;
    private String department;
    private Integer gender;
    private int id;
    private String job;
    private String name;
    private String profilePath;

    private Set<Movie> movies = new HashSet<Movie>();

    @Basic
    @Column(name = "credit_id")
    public String getCreditId() {
        return creditId;
    }

    public void setCreditId(String creditId) {
        this.creditId = creditId;
    }

    @Basic
    @Column(name = "department")
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
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
    @Column(name = "job")
    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
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
        Crew that = (Crew) o;
        return id == that.id &&
                Objects.equals(creditId, that.creditId) &&
                Objects.equals(department, that.department) &&
                Objects.equals(gender, that.gender) &&
                Objects.equals(job, that.job) &&
                Objects.equals(name, that.name) &&
                Objects.equals(profilePath, that.profilePath);
    }

    @Override
    public int hashCode() {
        return Objects.hash(creditId, department, gender, id, job, name, profilePath);
    }

    @JsonIgnore
    @ManyToMany(mappedBy = "crews")
    public Set<Movie> getMovies() {
        return movies;
    }

    public void setMovies(Set<Movie> movieEntities) {
        this.movies = movieEntities;
    }
}
