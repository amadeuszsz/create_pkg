cmake_minimum_required(VERSION 3.14)
project(hello_world)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

ament_auto_add_library(${PROJECT_NAME} SHARED
  include/hello_world/hello_world.hpp
  include/hello_world/visibility_control.hpp
  src/hello_world.cpp
)

ament_auto_add_library(${PROJECT_NAME}_node SHARED
  include/hello_world/hello_world_node.hpp
  src/hello_world_node.cpp
)

rclcpp_components_register_node(${PROJECT_NAME}_node
  PLUGIN "hello_world::HelloWorldNode"
  EXECUTABLE ${PROJECT_NAME}_node_exe
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  ament_add_ros_isolated_gtest(test_hello_world
    test/test_hello_world.cpp
  )
  ament_target_dependencies(test_hello_world ${TEST_SOURCES})
  target_link_libraries(test_hello_world ${PROJECT_NAME})
endif()

ament_auto_package(INSTALL_TO_SHARE
  launch
  config
)
