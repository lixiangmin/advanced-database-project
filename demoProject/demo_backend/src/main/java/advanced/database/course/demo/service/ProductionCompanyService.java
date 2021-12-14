package advanced.database.course.demo.service;


import java.lang.Integer;

import advanced.database.course.demo.entity.ProductionCompany;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:03
 */
public interface ProductionCompanyService {

    void save(ProductionCompany productionCompany);

    void deleteById(Integer id);

    ProductionCompany findById(Integer id);

    List<ProductionCompany> findAll();
}

