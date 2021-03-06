package dao

import (
    "fmt"
    "log"
    "errors"
    "gopkg.in/mgo.v2"
    "gopkg.in/mgo.v2/bson"
    "sona/broker/conf"
)

type ServiceData struct {
    ServiceKey string `bson:"serviceKey"`
    Version uint `bson:"version"`
    ConfKeys []string `bson:"confKeys"`
    ConfValues []string `bson:"confValues"`
}

//获取collection以便操作
func getCollection() (*mgo.Session, *mgo.Collection, error) {
    url := fmt.Sprintf("%s:%d", conf.GlobalConf.DbHost, conf.GlobalConf.DbPort)
    session, err := mgo.Dial(url)
    if err != nil {
        log.Printf("dial mongodb %s get %s\n", url, err)
        return nil, nil, err
    }

    collection := session.DB(conf.GlobalConf.DbName).C(conf.GlobalConf.DbCollectionName)
    if collection == nil {
        session.Close()
        errLog := fmt.Sprintf("no database %s or collection %s\n", conf.GlobalConf.DbName, conf.GlobalConf.DbCollectionName)
        log.Printf(errLog)
        return nil, nil, errors.New(errLog)
    }
    return session, collection, nil
}

//加载所有数据
func ReloadAllData() (map[string]*ServiceData, error) {
    log.Println("reload data from mongo db")
    session, collection, err := getCollection()
    if err != nil {
        return nil, err
    }
    defer session.Close()
    results := make([]ServiceData, 0)
    err = collection.Find(bson.M{}).All(&results)
    if err != nil {
        return nil, err
    }

    data := make(map[string]*ServiceData)
    /* 错误，result变量仅被创建了一次，导致&result一直指向同样的变量
    for _, result := range results {
        data[result.ServiceKey] = &result
    }
    */
    for i := 0;i < len(results);i++ {
        data[results[i].ServiceKey] = &results[i]
    }
    return data, nil
}

//新增数据，发起自admin添加
func AddDocument(serviceKey string, version uint, confKeys []string, confValues []string) error {
    session, collection, err := getCollection()
    if err != nil {
        return err
    }
    defer session.Close()
    return collection.Insert(&ServiceData{
        ServiceKey: serviceKey,
        Version: version,
        ConfKeys: confKeys,
        ConfValues: confValues,
    })
}

//获取数据
func GetDocument(serviceKey string) (uint, []string, []string, error) {
    session, collection, err := getCollection()
    if err != nil {
        return 0, nil, nil, err
    }
    defer session.Close()

    result := ServiceData{}
    err = collection.Find(bson.M{"serviceKey":serviceKey}).One(&result)
    if err != nil {
        return 0, nil, nil, err
    }
    return result.Version, result.ConfKeys, result.ConfValues, nil
}

//修改数据
func UpdateDocument(serviceKey string, version uint, confKeys []string, confValues []string) error {
    session, collection, err := getCollection()
    if err != nil {
        return err
    }
    defer session.Close()
    return collection.Update(bson.M{"serviceKey":serviceKey},
    &ServiceData{
        ServiceKey: serviceKey,
        Version: version,
        ConfKeys: confKeys,
        ConfValues: confValues,
    })
}