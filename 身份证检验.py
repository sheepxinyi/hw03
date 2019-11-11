/**
 * 二代身份证号码有效性校验
 *
 * @param idNo
 * @return
 */
public static boolean isValidIdNo(String idNo) {
  return isIdNoPattern(idNo) && isValidProvinceId(idNo.substring(0, 2))
      && isValidDate(idNo.substring(6, 14)) && checkIdNoLastNum(idNo);
}
————————————————
版权声明：本文为CSDN博主「逸笔草草」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/embracejava/article/details/77341740