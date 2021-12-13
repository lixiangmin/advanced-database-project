package advanced.database.course.demo.repository;


import java.lang.Integer;

import advanced.database.course.demo.entity.ProductionCompany;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * 持久层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:03
 */
@Repository
public interface ProductionCompanyRepository extends JpaRepository<ProductionCompany, Integer> {
    void deleteById(Integer id);

    ProductionCompany findOneById(Integer id);
}

