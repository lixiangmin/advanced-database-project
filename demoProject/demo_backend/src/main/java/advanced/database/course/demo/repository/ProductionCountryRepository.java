package advanced.database.course.demo.repository;


import java.lang.String;

import advanced.database.course.demo.entity.ProductionCountry;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * 持久层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:04
 */
@Repository
public interface ProductionCountryRepository extends JpaRepository<ProductionCountry, String> {
    void deleteByIso31661(String id);

    ProductionCountry findOneByIso31661(String id);
}

