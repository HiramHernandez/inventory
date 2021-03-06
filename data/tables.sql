PGDMP     (    &                y         	   inventory    12.6    12.6 !    3           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            4           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            5           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            6           1262    16393 	   inventory    DATABASE     ?   CREATE DATABASE inventory WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Mexico.1252' LC_CTYPE = 'Spanish_Mexico.1252';
    DROP DATABASE inventory;
                postgres    false                        2615    16394 
   inventario    SCHEMA        CREATE SCHEMA inventario;
    DROP SCHEMA inventario;
                postgres    false            ?            1259    16418    tienda    TABLE     ?   CREATE TABLE inventario.tienda (
    id_tienda integer NOT NULL,
    nombre character varying(50),
    direccion character varying(100)
);
    DROP TABLE inventario.tienda;
    
   inventario         heap    postgres    false    6            ?            1259    16416    tienda_id_tienda_seq1    SEQUENCE     ?   ALTER TABLE inventario.tienda ALTER COLUMN id_tienda ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME inventario.tienda_id_tienda_seq1
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
         
   inventario          postgres    false    204    6            ?            1259    16451    id_inventario_fisico_detalle    TABLE     ?   CREATE TABLE public.id_inventario_fisico_detalle (
    id_inventario_fisico_detalle integer NOT NULL,
    id_inventario_fisico integer NOT NULL,
    id_producto integer NOT NULL,
    cantidad integer,
    motivo character varying(50)
);
 0   DROP TABLE public.id_inventario_fisico_detalle;
       public         heap    postgres    false            ?            1259    16449 =   id_inventario_fisico_detalle_id_inventario_fisico_detalle_seq    SEQUENCE     '  ALTER TABLE public.id_inventario_fisico_detalle ALTER COLUMN id_inventario_fisico_detalle ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.id_inventario_fisico_detalle_id_inventario_fisico_detalle_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    216            ?            1259    16436    inventario_inicial    TABLE     g   CREATE TABLE public.inventario_inicial (
    id_inventario_inicial integer NOT NULL,
    fecha date
);
 &   DROP TABLE public.inventario_inicial;
       public         heap    postgres    false            ?            1259    16441    inventario_inicial_detalle    TABLE     ?   CREATE TABLE public.inventario_inicial_detalle (
    id_inventario_inicial_detalle integer NOT NULL,
    id_inventario_inicial integer NOT NULL,
    cantidad integer NOT NULL,
    id_producto integer NOT NULL
);
 .   DROP TABLE public.inventario_inicial_detalle;
       public         heap    postgres    false            ?            1259    16439 <   inventario_inicial_detalle_id_inventario_inicial_detalle_seq    SEQUENCE     %  ALTER TABLE public.inventario_inicial_detalle ALTER COLUMN id_inventario_inicial_detalle ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.inventario_inicial_detalle_id_inventario_inicial_detalle_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    212            ?            1259    16434 ,   inventario_inicial_id_inventario_inicial_seq    SEQUENCE       ALTER TABLE public.inventario_inicial ALTER COLUMN id_inventario_inicial ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.inventario_inicial_id_inventario_inicial_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    210            ?            1259    16446    invetario_fisico    TABLE     {   CREATE TABLE public.invetario_fisico (
    id_inventario_fisico integer NOT NULL,
    fecha date,
    id_tienda integer
);
 $   DROP TABLE public.invetario_fisico;
       public         heap    postgres    false            ?            1259    16444 )   invetario_fisico_id_inventario_fisico_seq    SEQUENCE     ?   ALTER TABLE public.invetario_fisico ALTER COLUMN id_inventario_fisico ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.invetario_fisico_id_inventario_fisico_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    214            ?            1259    16430 	   productos    TABLE     ?   CREATE TABLE public.productos (
    id_producto integer NOT NULL,
    nombre character varying(50) NOT NULL,
    sku character varying(50),
    precio real DEFAULT 0
);
    DROP TABLE public.productos;
       public         heap    postgres    false            ?            1259    16428    productos_id_producto_seq    SEQUENCE     ?   ALTER TABLE public.productos ALTER COLUMN id_producto ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.productos_id_producto_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    208            ?            1259    16425    tienda    TABLE     ?   CREATE TABLE public.tienda (
    id_tienda integer NOT NULL,
    nombre character varying(50),
    direccion character varying(100)
);
    DROP TABLE public.tienda;
       public         heap    postgres    false            ?            1259    16423    tienda_id_tienda_seq    SEQUENCE     ?   ALTER TABLE public.tienda ALTER COLUMN id_tienda ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.tienda_id_tienda_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    206            $          0    16418    tienda 
   TABLE DATA           B   COPY inventario.tienda (id_tienda, nombre, direccion) FROM stdin;
 
   inventario          postgres    false    204   X&       0          0    16451    id_inventario_fisico_detalle 
   TABLE DATA           ?   COPY public.id_inventario_fisico_detalle (id_inventario_fisico_detalle, id_inventario_fisico, id_producto, cantidad, motivo) FROM stdin;
    public          postgres    false    216   u&       *          0    16436    inventario_inicial 
   TABLE DATA           J   COPY public.inventario_inicial (id_inventario_inicial, fecha) FROM stdin;
    public          postgres    false    210   ?&       ,          0    16441    inventario_inicial_detalle 
   TABLE DATA           ?   COPY public.inventario_inicial_detalle (id_inventario_inicial_detalle, id_inventario_inicial, cantidad, id_producto) FROM stdin;
    public          postgres    false    212   ?&       .          0    16446    invetario_fisico 
   TABLE DATA           R   COPY public.invetario_fisico (id_inventario_fisico, fecha, id_tienda) FROM stdin;
    public          postgres    false    214   '       (          0    16430 	   productos 
   TABLE DATA           E   COPY public.productos (id_producto, nombre, sku, precio) FROM stdin;
    public          postgres    false    208   >'       &          0    16425    tienda 
   TABLE DATA           >   COPY public.tienda (id_tienda, nombre, direccion) FROM stdin;
    public          postgres    false    206   ?'       7           0    0    tienda_id_tienda_seq1    SEQUENCE SET     H   SELECT pg_catalog.setval('inventario.tienda_id_tienda_seq1', 1, false);
       
   inventario          postgres    false    203            8           0    0 =   id_inventario_fisico_detalle_id_inventario_fisico_detalle_seq    SEQUENCE SET     k   SELECT pg_catalog.setval('public.id_inventario_fisico_detalle_id_inventario_fisico_detalle_seq', 2, true);
          public          postgres    false    215            9           0    0 <   inventario_inicial_detalle_id_inventario_inicial_detalle_seq    SEQUENCE SET     j   SELECT pg_catalog.setval('public.inventario_inicial_detalle_id_inventario_inicial_detalle_seq', 2, true);
          public          postgres    false    211            :           0    0 ,   inventario_inicial_id_inventario_inicial_seq    SEQUENCE SET     Z   SELECT pg_catalog.setval('public.inventario_inicial_id_inventario_inicial_seq', 1, true);
          public          postgres    false    209            ;           0    0 )   invetario_fisico_id_inventario_fisico_seq    SEQUENCE SET     W   SELECT pg_catalog.setval('public.invetario_fisico_id_inventario_fisico_seq', 1, true);
          public          postgres    false    213            <           0    0    productos_id_producto_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.productos_id_producto_seq', 2, true);
          public          postgres    false    207            =           0    0    tienda_id_tienda_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.tienda_id_tienda_seq', 11, true);
          public          postgres    false    205            $      x?????? ? ?      0   5   x?3?4B]SN_? _G.# ?8??}????\]]???b???? ?h	?      *      x?3?4202?50?52?????? ??      ,      x?3?4?445?4?2???,#?=... ,H      .      x?3?4202?50?52?4?????? "?      (   =   x?3?t??S?VuR?4Pp??0?@N#s=3c.#4EF`U?&&?Ɯ&\1z\\\ eX      &   ?   x???K?0D??)|?B(???BFi,%????? Q???+K3o???W?	+`??3?*?K?z(2?K??	֞`o*`^
??DՕ?w2?W?ԟ??6C`???T0I??)??s=?Օ62"????z̴?6F??;h??ץ     