cmake_minimum_required(VERSION 3.14)
project(hello_world)

find_package(autoware_cmake REQUIRED)
ament_auto_find_build_dependencies(REQUIRED
  ${${PROJECT_NAME}_BUILD_DEPENDS}
  ${${PROJECT_NAME}_BUILDTOOL_DEPENDS}
)

autoware_package()

set(HELLO_WORLD_LIB_SRC
  src/hello_world.cpp
)

set(HELLO_WORLD_LIB_HEADERS
  include/hello_world/hello_world.hpp
  include/hello_world/visibility_control.hpp
)

ament_auto_add_library(${PROJECT_NAME} SHARED
  ${HELLO_WORLD_LIB_SRC}
  ${HELLO_WORLD_LIB_HEADERS}
)

set(HELLO_WORLD_NODE_SRC
  src/hello_world_node.cpp
)

set(HELLO_WORLD_NODE_HEADERS
  include/hello_world/hello_world_node.hpp
)

ament_auto_add_library(${PROJECT_NAME}_node SHARED
  ${HELLO_WORLD_NODE_SRC}
  ${HELLO_WORLD_NODE_HEADERS}
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
