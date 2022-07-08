# 实验三（第4题）

4. 模拟快餐订餐场景

   - 定义 4 个类：Customer 顾客类，Employee 商户类，Food 食物类 以及 Lunch 订餐管理。

   - Lunch 类包含 Customer 和 Employee 实例，具有下单 order 方法，该方法要求 Customer 实例调用自身的 placeOrder 向 Employee 对象要求下单，并且获得 Employee 对象调用 takeOrder 生成和返回一个 Food 对象，Food 对象应当包含了食物名字符串。调用关系如下：

     Lunch.order—〉Customer.placeOrder—〉Employee.takeOrder—〉Food
     
   - Lunch 类包含 result 方法，要求 Customer 打印所收到的食物订单。

   - 编写交互式界面验证所设计的订餐系统。