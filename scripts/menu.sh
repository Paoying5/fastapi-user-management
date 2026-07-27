#!/usr/bin/env bash


# ==========================================
# FastAPI User Management
# Docker Development Menu
# ==========================================


# ---------- Colors ----------

GREEN="\033[0;32m"
RED="\033[0;31m"
BLUE="\033[0;34m"
YELLOW="\033[1;33m"
CYAN="\033[0;36m"
NC="\033[0m"


# ---------- Project Config ----------

API_SERVICE="api"
DB_SERVICE="postgres"

DB_USER="admin"
DB_NAME="fastapi_db"



# ---------- Helper Functions ----------


pause()
{
    echo
    read -p "Press Enter to continue..."
}


check_docker()
{

    if ! command -v docker >/dev/null 2>&1
    then
        echo -e "${RED}Docker is not installed.${NC}"
        exit 1
    fi


    if ! docker compose version >/dev/null 2>&1
    then
        echo -e "${RED}Docker Compose is not available.${NC}"
        exit 1
    fi

}



success()
{
    echo -e "${GREEN}$1${NC}"
}


error()
{
    echo -e "${RED}$1${NC}"
}


info()
{
    echo -e "${BLUE}$1${NC}"
}



# ---------- Docker Actions ----------


start_project()
{
    info "Starting containers..."

    docker compose up --build -d

    success "Project started."
}



stop_project()
{
    info "Stopping containers..."

    docker compose down

    success "Containers stopped."
}



restart_project()
{
    info "Restarting containers..."

    docker compose down

    docker compose up --build -d

    success "Project restarted."
}



rebuild_project()
{
    info "Rebuilding containers..."

    docker compose build --no-cache

    docker compose up -d

    success "Rebuild completed."
}



view_logs()
{
    info "Showing logs..."

    docker compose logs -f
}



app_shell()
{

    info "Opening FastAPI container shell..."


    docker compose exec $API_SERVICE bash \
    || docker compose exec $API_SERVICE sh

}



postgres_shell()
{

    info "Opening PostgreSQL shell..."


    docker compose exec \
    $DB_SERVICE \
    psql \
    -U $DB_USER \
    -d $DB_NAME

}



# ---------- Database ----------


reset_database()
{

    echo -e "${YELLOW}"
    echo "WARNING:"
    echo "This will delete PostgreSQL volume."
    echo "All database data will be removed."
    echo -e "${NC}"


    read -p "Continue? (y/N): " answer


    if [[ "$answer" == "y" ]]
    then

        docker compose down -v

        docker compose up --build -d

        success "Database reset completed."

    else

        info "Cancelled."

    fi

}



alembic_upgrade()
{

    info "Running Alembic upgrade..."

    docker compose exec \
    $API_SERVICE \
    alembic upgrade head

}



alembic_revision()
{

    read -p "Migration message: " msg


    docker compose exec \
    $API_SERVICE \
    alembic revision --autogenerate -m "$msg"

}



alembic_downgrade()
{

    docker compose exec \
    $API_SERVICE \
    alembic downgrade -1

}



# ---------- Docker Utilities ----------


show_containers()
{
    docker compose ps
}



show_images()
{
    docker images
}



show_volumes()
{
    docker volume ls
}



show_networks()
{
    docker network ls
}



clean_docker()
{

    echo -e "${YELLOW}"
    echo "This removes unused Docker resources."
    echo -e "${NC}"


    read -p "Continue? (y/N): " answer


    if [[ "$answer" == "y" ]]
    then

        docker system prune -f

        success "Docker cleanup completed."

    else

        info "Cancelled."

    fi

}



build_only()
{

    docker compose build

    success "Build completed."

}



install_requirements()
{

    info "Installing Python requirements..."

    docker compose exec \
    $API_SERVICE \
    pip install -r requirements.txt


}



# ---------- Menu ----------


show_menu()
{

clear


echo -e "${CYAN}"
echo "========================================="
echo "     FastAPI User Management"
echo "     Docker Development Menu"
echo "========================================="
echo -e "${NC}"


echo " Docker"
echo "-----------------------------------------"
echo "1.  Start Containers"
echo "2.  Stop Containers"
echo "3.  Restart Containers"
echo "4.  Rebuild Containers"
echo


echo " Development"
echo "-----------------------------------------"
echo "5.  View Logs"
echo "6.  App Shell"
echo "7.  PostgreSQL Shell"
echo


echo " Database"
echo "-----------------------------------------"
echo "8.  Reset Database"
echo "9.  Alembic Upgrade"
echo "10. Create Migration"
echo "11. Alembic Downgrade"
echo


echo " Docker Utilities"
echo "-----------------------------------------"
echo "12. Show Containers"
echo "13. Show Images"
echo "14. Show Volumes"
echo "15. Show Networks"
echo "16. Clean Docker"
echo


echo " Others"
echo "-----------------------------------------"
echo "17. Build Only"
echo "18. Install Requirements"
echo


echo "0. Exit"

echo

}



# ---------- Main Loop ----------


check_docker


while true
do

show_menu


read -p "Choose option: " choice


case $choice in


1)
start_project
pause
;;


2)
stop_project
pause
;;


3)
restart_project
pause
;;


4)
rebuild_project
pause
;;


5)
view_logs
;;


6)
app_shell
;;


7)
postgres_shell
pause
;;


8)
reset_database
pause
;;


9)
alembic_upgrade
pause
;;


10)
alembic_revision
pause
;;


11)
alembic_downgrade
pause
;;


12)
show_containers
pause
;;


13)
show_images
pause
;;


14)
show_volumes
pause
;;


15)
show_networks
pause
;;


16)
clean_docker
pause
;;


17)
build_only
pause
;;


18)
install_requirements
pause
;;


0)
echo "Goodbye!"
exit 0
;;


*)
error "Invalid option."
pause
;;

esac


done