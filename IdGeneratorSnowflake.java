package com.ruoyi.common.exception;

import cn.hutool.core.lang.Snowflake;
import cn.hutool.core.net.NetUtil;
import cn.hutool.core.util.IdUtil;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;

/**
 * @author cVzhanshi
 * @create 2021-08-19 0:06
 */
@Component
public class IdGeneratorSnowflake {

    private static long workerId = 0;  //第几号机房
    private static long datacenterId = 1;  //第几号机器
    private static Snowflake snowflake = IdUtil.getSnowflake(workerId, datacenterId);

    @PostConstruct  //构造后开始执行，加载初始化工作
    public void init(){
        try{
            //获取本机的ip地址编码
            workerId = NetUtil.ipv4ToLong(NetUtil.getLocalhostStr());
        }catch (Exception e){
            e.printStackTrace();
            workerId = NetUtil.getLocalhostStr().hashCode();
        }
    }

    public synchronized static long snowflakeId(){
        return snowflake.nextId();
    }

    public synchronized long snowflakeId(long workerId, long datacenterId){
        Snowflake snowflake = IdUtil.createSnowflake(workerId, datacenterId);
        return snowflake.nextId();
    }

    //测试

}
