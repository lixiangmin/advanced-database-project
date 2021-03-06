package advanced.database.course.demo.repository;


import java.lang.Integer;
import java.util.List;

import advanced.database.course.demo.entity.Movie;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

/**
 * 持久层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:02
 */
@Repository
public interface MovieRepository extends JpaRepository<Movie, Integer> {
    void deleteById(Integer id);

    Movie findOneById(Integer id);

    @Query(nativeQuery = true, value = "select * from movie where movie.score is not null order by movie.score DESC limit 9")
    List<Movie> findRecommendMovies();

    @Query(nativeQuery = true, value = "select * from movie where movie.title like %:text% or movie.original_title like  %:text% or movie.overview like %:text% order by movie.score DESC")
    Page<Movie> searchMoviesByText(@Param("text") String text, Pageable pageable);

    @Query(nativeQuery = true, value = "select * from (select genre_id,movie_id  from `movie_genre` inner join genre on movie_genre.genre_id = genre.id ) t1 " +
            "inner join movie on t1.movie_id = movie.id WHERE t1.genre_id = :genreId group by movie.id order by movie.score DESC")
    Page<Movie> searchMoviesByGenreId(@Param("genreId") int genreId, Pageable pageable);

    @Query(nativeQuery = true, value = "select * from " +
            "(select movie_id FROM " +
            "(select user_id from `rating` where movie_id = :movieId limit 20) `t1` " +
            "inner join `rating` on `rating`.user_id = `t1`.user_id) `t2` " +
            "inner join `movie` on `movie`.id = `t2`.movie_id where `movie`.id != :movieId group by `movie`.id order by `movie`.score DESC")
    Page<Movie> searchMoviesByMovieId(@Param("movieId") int movieId, Pageable pageRequest);
}

