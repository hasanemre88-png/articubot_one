from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # KODDA DEĞİŞTİ: USB sırası değişirse launch komutundan port verilebilir.
    serial_port = LaunchConfiguration('serial_port')

    return LaunchDescription([
        DeclareLaunchArgument(
            'serial_port',
            default_value='/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_50afdc5f5d316a4680971c939177bba2-if00-port0',  # KODDA DEĞİŞTİ: RPLIDAR CP2102 kalıcı cihaz yolu
            description='RPLIDAR A2M12 serial port'
        ),

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': serial_port,  # KODDA DEĞİŞTİ
                'serial_baudrate': 256000,  # KODDA DEĞİŞTİ: A2M12 baud rate
                'frame_id': 'laser_frame',
                'inverted': False,  # KODDA DEĞİŞTİ: Açıkça belirtildi
                'angle_compensate': True,
                'scan_mode': 'Standard'
            }]
        )
    ])