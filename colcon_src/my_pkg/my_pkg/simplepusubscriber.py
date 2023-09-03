import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Sim_sub(Node):
    def __init__(self):
        super().__init__('simple_msub')
        self.pub = self.create_subscription(String, 'message', self.sub, 10)

    def sub(self, msg):
        # print(msg.data)
        self.get_logger().info(msg.data)
        # self.get_logger().error(msg.data)

def main():
    rclpy.init()
    node = Sim_sub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('keyboard Interrupt!!')
    finally:
        node.destroy_node
        rclpy.shutdown()

if __name__ == '__main__':
    main()