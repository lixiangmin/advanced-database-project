package advanced.database.course.demo.entity;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity
@Table(name = "movie")
public class Movie {
    private String adult;
    private Double budget;
    private String homepage;
    private int id;
    private String imdbId;
    private String originalLanguage;
    private String originalTitle;
    private String overview;
    private Double popularity;
    private String posterPath;
    private String releaseDate;
    private Double revenue;
    private Double runtime;
    private String status;
    private String tagline;
    private String title;
    private String video;
    private Double voteAverage;
    private Integer voteCount;

    private Set<Cast> casts = new HashSet<Cast>();

    private Set<Crew> crews = new HashSet<Crew>();

    private Set<Genre> genres = new HashSet<Genre>();

    private Set<Keyword> keywords = new HashSet<Keyword>();

    private Set<ProductionCountry> productionCountries = new HashSet<ProductionCountry>();

    private Set<ProductionCompany> productionCompanies = new HashSet<ProductionCompany>();

    private Set<SpokenLanguage> spokenLanguages = new HashSet<SpokenLanguage>();


    @Basic
    @Column(name = "adult")
    public String getAdult() {
        return adult;
    }

    public void setAdult(String adult) {
        this.adult = adult;
    }

    @Basic
    @Column(name = "budget")
    public Double getBudget() {
        return budget;
    }

    public void setBudget(Double budget) {
        this.budget = budget;
    }

    @Basic
    @Column(name = "homepage")
    public String getHomepage() {
        return homepage;
    }

    public void setHomepage(String homepage) {
        this.homepage = homepage;
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
    @Column(name = "imdb_id")
    public String getImdbId() {
        return imdbId;
    }

    public void setImdbId(String imdbId) {
        this.imdbId = imdbId;
    }

    @Basic
    @Column(name = "original_language")
    public String getOriginalLanguage() {
        return originalLanguage;
    }

    public void setOriginalLanguage(String originalLanguage) {
        this.originalLanguage = originalLanguage;
    }

    @Basic
    @Column(name = "original_title")
    public String getOriginalTitle() {
        return originalTitle;
    }

    public void setOriginalTitle(String originalTitle) {
        this.originalTitle = originalTitle;
    }

    @Basic
    @Column(name = "overview")
    public String getOverview() {
        return overview;
    }

    public void setOverview(String overview) {
        this.overview = overview;
    }

    @Basic
    @Column(name = "popularity")
    public Double getPopularity() {
        return popularity;
    }

    public void setPopularity(Double popularity) {
        this.popularity = popularity;
    }

    @Basic
    @Column(name = "poster_path")
    public String getPosterPath() {
        return posterPath;
    }

    public void setPosterPath(String posterPath) {
        this.posterPath = posterPath;
    }

    @Basic
    @Column(name = "release_date")
    public String getReleaseDate() {
        return releaseDate;
    }

    public void setReleaseDate(String releaseDate) {
        this.releaseDate = releaseDate;
    }

    @Basic
    @Column(name = "revenue")
    public Double getRevenue() {
        return revenue;
    }

    public void setRevenue(Double revenue) {
        this.revenue = revenue;
    }

    @Basic
    @Column(name = "runtime")
    public Double getRuntime() {
        return runtime;
    }

    public void setRuntime(Double runtime) {
        this.runtime = runtime;
    }

    @Basic
    @Column(name = "status")
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    @Basic
    @Column(name = "tagline")
    public String getTagline() {
        return tagline;
    }

    public void setTagline(String tagline) {
        this.tagline = tagline;
    }

    @Basic
    @Column(name = "title")
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    @Basic
    @Column(name = "video")
    public String getVideo() {
        return video;
    }

    public void setVideo(String video) {
        this.video = video;
    }

    @Basic
    @Column(name = "vote_average")
    public Double getVoteAverage() {
        return voteAverage;
    }

    public void setVoteAverage(Double voteAverage) {
        this.voteAverage = voteAverage;
    }

    @Basic
    @Column(name = "vote_count")
    public Integer getVoteCount() {
        return voteCount;
    }

    public void setVoteCount(Integer voteCount) {
        this.voteCount = voteCount;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Movie that = (Movie) o;
        return id == that.id &&
                Objects.equals(adult, that.adult) &&
                Objects.equals(budget, that.budget) &&
                Objects.equals(homepage, that.homepage) &&
                Objects.equals(imdbId, that.imdbId) &&
                Objects.equals(originalLanguage, that.originalLanguage) &&
                Objects.equals(originalTitle, that.originalTitle) &&
                Objects.equals(overview, that.overview) &&
                Objects.equals(popularity, that.popularity) &&
                Objects.equals(posterPath, that.posterPath) &&
                Objects.equals(releaseDate, that.releaseDate) &&
                Objects.equals(revenue, that.revenue) &&
                Objects.equals(runtime, that.runtime) &&
                Objects.equals(status, that.status) &&
                Objects.equals(tagline, that.tagline) &&
                Objects.equals(title, that.title) &&
                Objects.equals(video, that.video) &&
                Objects.equals(voteAverage, that.voteAverage) &&
                Objects.equals(voteCount, that.voteCount);
    }

    @Override
    public int hashCode() {
        return Objects.hash(adult, budget, homepage, id, imdbId, originalLanguage, originalTitle, overview, popularity, posterPath, releaseDate, revenue, runtime, status, tagline, title, video, voteAverage, voteCount);
    }

    @JsonIgnoreProperties(value = {"movies"})
    @ManyToMany(targetEntity = Cast.class, cascade = CascadeType.ALL)
    @JoinTable(name = "movie_cast",
            joinColumns = {@JoinColumn(name = "movieId", referencedColumnName = "id")},
            inverseJoinColumns = {@JoinColumn(name = "castId", referencedColumnName = "id")}
    )
    public Set<Cast> getCasts() {
        return casts;
    }

    public void setCasts(Set<Cast> castEntities) {
        this.casts = castEntities;
    }

    @JsonIgnoreProperties(value = {"movies"})
    @ManyToMany(targetEntity = Crew.class, cascade = CascadeType.ALL)
    @JoinTable(name = "movie_crew",
            joinColumns = {@JoinColumn(name = "movieId", referencedColumnName = "id")},
            inverseJoinColumns = {@JoinColumn(name = "crewId", referencedColumnName = "id")}
    )
    public Set<Crew> getCrews() {
        return crews;
    }

    public void setCrews(Set<Crew> crewEntities) {
        this.crews = crewEntities;
    }

    @JsonIgnoreProperties(value = {"movies"})
    @ManyToMany(targetEntity = Genre.class, cascade = CascadeType.ALL)
    @JoinTable(name = "movie_genre",
            joinColumns = {@JoinColumn(name = "movieId", referencedColumnName = "id")},
            inverseJoinColumns = {@JoinColumn(name = "genreId", referencedColumnName = "id")}
    )
    public Set<Genre> getGenres() {
        return genres;
    }

    public void setGenres(Set<Genre> genreEntities) {
        this.genres = genreEntities;
    }

    @JsonIgnoreProperties(value = {"movies"})
    @ManyToMany(targetEntity = Keyword.class, cascade = CascadeType.ALL)
    @JoinTable(name = "movie_keyword",
            joinColumns = {@JoinColumn(name = "movieId", referencedColumnName = "id")},
            inverseJoinColumns = {@JoinColumn(name = "keywordId", referencedColumnName = "id")}
    )
    public Set<Keyword> getKeywords() {
        return keywords;
    }

    public void setKeywords(Set<Keyword> keywordEntities) {
        this.keywords = keywordEntities;
    }

    @JsonIgnoreProperties(value = {"movies"})
    @ManyToMany(targetEntity = ProductionCountry.class, cascade = CascadeType.ALL)
    @JoinTable(name = "movie_production_country",
            joinColumns = {@JoinColumn(name = "movieId", referencedColumnName = "id")},
            inverseJoinColumns = {@JoinColumn(name = "iso_3166_1", referencedColumnName = "iso_3166_1")}
    )
    public Set<ProductionCountry> getProductionCountries() {
        return productionCountries;
    }

    public void setProductionCountries(Set<ProductionCountry> productionCountries) {
        this.productionCountries = productionCountries;
    }

    @JsonIgnoreProperties(value = {"movies"})
    @ManyToMany(targetEntity = ProductionCompany.class, cascade = CascadeType.ALL)
    @JoinTable(name = "movie_production_company",
            joinColumns = {@JoinColumn(name = "movieId", referencedColumnName = "id")},
            inverseJoinColumns = {@JoinColumn(name = "productionCompanyId", referencedColumnName = "id")}
    )
    public Set<ProductionCompany> getProductionCompanies() {
        return productionCompanies;
    }

    public void setProductionCompanies(Set<ProductionCompany> productionCompanies) {
        this.productionCompanies = productionCompanies;
    }

    @JsonIgnoreProperties(value = {"movies"})
    @ManyToMany(targetEntity = SpokenLanguage.class, cascade = CascadeType.ALL)
    @JoinTable(name = "movie_spoken_language",
            joinColumns = {@JoinColumn(name = "movieId", referencedColumnName = "id")},
            inverseJoinColumns = {@JoinColumn(name = "iso_639_1", referencedColumnName = "iso_639_1")}
    )
    public Set<SpokenLanguage> getSpokenLanguages() {
        return spokenLanguages;
    }

    public void setSpokenLanguages(Set<SpokenLanguage> spokenLanguages) {
        this.spokenLanguages = spokenLanguages;
    }
}
