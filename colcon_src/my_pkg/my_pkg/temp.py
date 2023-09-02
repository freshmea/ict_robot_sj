import rclpy
from rclpy.node import Node 
def test():
    print('test')

def main():
    rclpy.init()
    node = Node('test')
    node.create_timer(1, test)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('keyboard Interrupt!!')
    finally:
        node.destroy_node
        rclpy.shutdown()

if __name__ == '__main__':
    main()