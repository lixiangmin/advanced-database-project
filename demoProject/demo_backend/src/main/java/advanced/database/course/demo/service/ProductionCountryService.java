package advanced.database.course.demo.service;


import java.lang.String;

import advanced.database.course.demo.entity.ProductionCountry;

import java.util.Collection;
import java.util.List;


/**
 * 业务层
 *
 * @author lixiangmin
 * @since 2021-12-13 13:00:04
 */
public interface ProductionCountryService {

    void save(ProductionCountry productionCountry);

    void deleteById(String id);

    ProductionCountry findById(String id);

    List<ProductionCountry> findAll();
}

